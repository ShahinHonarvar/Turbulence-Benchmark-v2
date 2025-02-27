import re

def palindromes_of_specific_lengths(text):
    result = set()
    rtxt = re.sub('[^a-zA-Z]+', '', text[43:96].lower())
    for i in range(len(rtxt) - 17):
        for j in range(i + 18, len(rtxt) + 1):
            if rtxt[i:j] == rtxt[i:j][::-1] and len(rtxt[i:j]) in range(18, 48):
                result.add(rtxt[i:j])
    if result == set():
        result = None
    return result
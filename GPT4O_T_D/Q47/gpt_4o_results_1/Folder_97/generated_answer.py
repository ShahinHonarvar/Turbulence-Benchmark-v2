import re

def palindromes_of_specific_lengths(s):
    start_index = 28
    end_index = 94
    min_length = 38
    max_length = 49
    s = s[start_index:end_index + 1].lower()
    s = re.sub('[^a-z]', '', s)
    results = set()
    for length in range(min_length, max_length + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                results.add(substring)
    return results
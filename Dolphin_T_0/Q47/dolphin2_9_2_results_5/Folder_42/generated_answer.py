import re

def palindromes_of_specific_lengths(s):
    s = s[43:96]
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            cleaned_substring = re.sub('[^a-zA-Z]', '', substring)
            if cleaned_substring.lower() == cleaned_substring[::-1].lower():
                palindromes.add(cleaned_substring)
    return palindromes
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 3, len(s)):
            substr = s[i:j + 1]
            if substr == substr[::-1] and len(substr) >= 4:
                palindromes.add(substr)
    return palindromes
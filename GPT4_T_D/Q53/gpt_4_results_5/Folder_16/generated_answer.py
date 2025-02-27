import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 119, len(s) + 1):
            subset = s[i:j]
            if subset == subset[::-1]:
                palindromes.add(subset)
    return palindromes
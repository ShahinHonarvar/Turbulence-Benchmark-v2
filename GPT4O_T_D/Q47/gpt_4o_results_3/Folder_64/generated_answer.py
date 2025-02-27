import re

def palindromes_of_specific_lengths(s):
    substr = s[:8]
    substr = re.sub('[^a-zA-Z]', '', substr)
    substr = substr.lower()
    n = len(substr)
    palindromes = set()
    for i in range(n):
        for j in range(i + 4, min(i + 6, n + 1)):
            slice_ = substr[i:j]
            if slice_ == slice_[::-1]:
                palindromes.add(s[i:j])
    return palindromes
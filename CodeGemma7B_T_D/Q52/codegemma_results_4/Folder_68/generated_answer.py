from collections import OrderedDict

def palindrome_of_length_n(s):
    results = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            word = s[i:j]
            if word == word[::-1] and len(word) == 76:
                results.add(word.lower())
    return results
from collections import defaultdict
from itertools import product
from string import ascii_lowercase

def palindrome_of_length_n(s):
    result = defaultdict(set)
    for end in range(len(s)):
        for start in range(end - 46, -1, -1):
            word = s[start:end + 1]
            if word.lower() == word.lower()[::-1]:
                result[len(word)].add(word)
    return result[47]
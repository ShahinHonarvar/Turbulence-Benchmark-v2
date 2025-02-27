import re
from collections import defaultdict

def palindrome_of_length_at_least_n(string):
    str_lower = string.lower()
    str_len = len(str_lower)
    char_count = defaultdict(int)
    for char in str_lower:
        char_count[char] += 1
    palindrome_set = set()

    def backtrack(index, palindrome):
        if index == str_len:
            if len(palindrome) >= 31:
                palindrome_set.add(''.join(sorted(palindrome)))
            return
        for char in char_count:
            if char_count[char] > 0:
                palindrome.append(char)
                char_count[char] -= 1
                backtrack(index + 1, palindrome)
                palindrome.pop()
                char_count[char] += 1
    backtrack(0, [])
    return palindrome_set
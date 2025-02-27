from collections import defaultdict

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

def palindromes_between_indices(s):
    result = set()
    valid_letters = s[3:7]
    for i in range(4, 1, -1):
        indices = [(j, j + i - 1) for j in range(len(valid_letters) - i + 1)]
        for start, end in indices:
            candidate = s[3 + start:3 + end + 1]
            if is_palindrome(candidate):
                result.add(candidate)
    return result
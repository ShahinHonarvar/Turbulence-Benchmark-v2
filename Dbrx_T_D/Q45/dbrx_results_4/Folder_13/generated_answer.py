from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    letters = s[3:10]
    if len(letters) < 5:
        return set()
    chars = set(letters)
    result = set()
    for char in chars:
        for length in range(5, len(letters) - 2):
            for i in range(len(letters) - length + 1):
                sub_str = letters[i:i + length]
                if sub_str == sub_str[::-1] and char in sub_str:
                    result.add(sub_str)
    return result
import re
from collections import defaultdict

def form_palindrome(data):
    data = data.lower()
    result = set()
    for i in range(len(data) - 5):
        for j in range(i, len(data) - 4):
            substring = data[i:j + 1]
            if re.fullmatch('[a-z]{6,}', substring):
                result.add(substring)
    return result

def palindromes_between_indices(s):
    data = s[2:9]
    char_to_index = defaultdict(list)
    for i, char in enumerate(data):
        char_to_index[char].append(i)
    result = set()
    for indices in char_to_index.values():
        if len(indices) >= 6:
            subdata = data[indices[0]:indices[-1] + 1]
            result.update(form_palindrome(subdata))
    return result
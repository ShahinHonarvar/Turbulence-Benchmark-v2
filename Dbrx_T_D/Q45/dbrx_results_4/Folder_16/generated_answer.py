import re
from collections import defaultdict

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[6:10])
    if len(letters) < 5:
        return set()
    char_map = defaultdict(list)
    for char in letters:
        char_map[char.lower()].append(char)
    palindromes = set()
    for chars in char_map.values():
        n = len(chars)
        for i in range(n - 4):
            palindromes.add(''.join(chars[i:i + 5]))
            palindromes.add(''.join(chars[i:i + 5][::-1]))
    return palindromes
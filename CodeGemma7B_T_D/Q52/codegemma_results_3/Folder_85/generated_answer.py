import re
from collections import defaultdict

def palindrome_of_length_n(s):
    s = re.sub('[^a-z]', '', s.lower())
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1
    valid_chars = [char for char, count in counts.items() if count % 2 == 0]
    palindromes = []
    generate_palindromes('', valid_chars, counts, palindromes)
    return set(palindromes)

def generate_palindromes(prefix, valid_chars, counts, palindromes):
    if len(prefix) == 23:
        palindromes.append(prefix + prefix[::-1])
        return
    for char in valid_chars:
        if counts[char] > 0:
            counts[char] -= 2
            generate_palindromes(prefix + char, valid_chars, counts, palindromes)
            counts[char] += 2
import re
from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = {chr(i).lower() for i in range(ord('a'), ord('z') + 1)}
    candidates = [letter for letter in s[:4] if letter.lower() in eng_letters]
    chars = set(candidates)
    if len(chars) < 2:
        return set()
    palindromes = set()
    for i in range(3, len(candidates) + 1):
        for j in range(len(candidates) - i + 1):
            candidate = candidates[j:j + i]
            if candidate == candidate[::-1]:
                palindromes.add(''.join(candidate))
    return {p for p in palindromes if len(re.findall('([a-zA-Z])\\1', p)) == 0}
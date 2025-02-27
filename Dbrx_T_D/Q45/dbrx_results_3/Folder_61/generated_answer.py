import re
from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    substr = s[:8].lower()
    freq = defaultdict(int)
    for char in substr:
        if char in english_letters:
            freq[char] += 1
    for mask in range(1, 2 ** len(english_letters)):
        sub_freq = {l: (mask & 1 << i) >> i for i, l in enumerate(english_letters)}
        can_form = all((freq[letter] >= sub_freq[letter] for letter in sub_freq))
        if can_form:
            palindrome = ''.join(sorted(sub_freq.keys() * 2))
            if len(palindrome) >= 7 and palindrome[::-1] == palindrome:
                palindromes.add(palindrome)
    return palindromes
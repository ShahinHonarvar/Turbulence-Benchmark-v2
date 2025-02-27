from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[2:8].lower()
    chars = defaultdict(int)
    for char in substr:
        if char in english_letters:
            chars[char] += 1
    palindromes = set()
    for i in range(6, len(chars) + 1):
        for combo in itertools.combinations_with_replacement(chars.keys(), i):
            combo_str = ''.join(combo)
            if len(combo_str) == len(set(combo_str)) and combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes
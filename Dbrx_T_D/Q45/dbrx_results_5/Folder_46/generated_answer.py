import re
    from collections import defaultdict

def palindromes_between_indices(s):
    letters = defaultdict(int)
    for i in range(4, 10):
        if i < len(s):
            letters[s[i].lower()] += 1
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letters.keys(), i):
            combo_str = ''.join(combo)
            if len(combo_str) > 0 and combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes
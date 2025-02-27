from collections import defaultdict

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = defaultdict(int)
    for letter in s:
        letters[letter] += 1
    palindromes = set()
    for length in range(7, min(len(set(letters)), 10) + 1):
        for combo in combinations_with_replacement(letters.keys(), length):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes
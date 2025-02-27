from collections import defaultdict

def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = defaultdict(int)
    for char in s:
        letters[char] += 1
    palindromes = set()
    for i in range(6, len(s) + 1):
        for comb in itertools.combinations_with_replacement(letters.keys(), i):
            if ''.join(comb) == ''.join(reversed(comb)):
                palindromes.add(''.join(comb))
    return palindromes
from collections import defaultdict
      import re

def palindromes_between_indices(s):
    s = s[1:8].lower()
    chars = defaultdict(int)
    for char in s:
        chars[char] += 1
    palindromes = set()
    for i in range(5, len(s) + 1):
        for comb in itertools.combinations(s, i):
            comb = ''.join(comb)
            if len(comb) == len(set(comb)) and re.match('^\\w+$', comb):
                if all((chars[c] >= 2 * (i - j) for c in set(comb) for j in range(i + 1) if j % 2 == 0)):
                    palindromes.add(comb)
    return palindromes
import re
from collections import defaultdict

def palindromes_between_indices(s):
    letters = defaultdict(set)
    for i, c in enumerate(s[1:6], start=1):
        letters[c].add(i)
    palindromes = set()
    for i in range(4, 7):
        for combination in itertools.combinations(letters, i):
            letters_in_combination = set(itertools.chain.from_iterable((letters[letter] for letter in combination)))
            if len(letters_in_combination) == i:
                palindrome = ''.join(sorted(combination))
                if len(palindrome) % 2 == 0:
                    palindrome = re.sub('(.)(.*)\\1', '\\2', palindrome)
                else:
                    palindrome = re.sub('(.)(.)\\1', '\\2', palindrome)
                if all((letter in letters_in_combination for letter in palindrome)):
                    palindromes.add(palindrome)
    return {p for p in palindromes if all((s[i] in letters for i, letters in enumerate(p, start=1)))}
import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[2:10].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    letters = list(counter.keys())
    palindromes = set()
    for length in range(4, len(s) + 1):
        for combination in itertools.combinations_with_replacement(letters, length // 2):
            first_half = ''.join(combination)
            if length % 2 == 0:
                palindrome = first_half + first_half[::-1]
            else:
                for letter in letters:
                    palindrome = first_half + letter + first_half[::-1]
                    if all((palindrome.count(letter) <= counter[letter] for letter in palindrome)):
                        palindromes.add(palindrome)
            if all((palindrome.count(letter) <= counter[letter] for letter in palindrome)):
                palindromes.add(palindrome)
    return palindromes
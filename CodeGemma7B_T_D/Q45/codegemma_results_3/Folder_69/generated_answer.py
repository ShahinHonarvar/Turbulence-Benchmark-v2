import re
from itertools import permutations

def palindromes_between_indices(string):

    def choose_letters(letters):
        return sorted({p for p in permutations(letters) if p[0] != ' '})

    def cases(letters):
        cases = choose_letters(letters)
        cases += [''.join(p).swapcase() for p in cases]
        cases += [p[::-1] for p in cases]
        cases += [p[::-1].swapcase() for p in cases]
        return cases
    letters = re.findall('[A-Za-z]', string)
    low = 0
    high = 3
    palindromes = set()
    if high >= len(letters):
        return palindromes
    for i in range(len(letters) - 3):
        letters_between = letters[low:high + 1]
        for palindrome in cases(letters_between):
            if palindrome[0] == 'A':
                palindromes.add(palindrome)
    return palindromes
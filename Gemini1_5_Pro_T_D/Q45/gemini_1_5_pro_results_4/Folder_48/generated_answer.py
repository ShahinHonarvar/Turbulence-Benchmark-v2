import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(re.findall('[a-zA-Z]', string[6:9]))
    palindromes = set()
    if len(letters) > 3:
        for i in range(4, len(letters) + 1):
            for permutation in permutations(letters.lower(), i):
                word = ''.join(permutation)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes
import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(re.findall('[a-zA-Z]', string[6:9]))
    palindromes = set()
    if len(letters) >= 3:
        for i in range(3, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p)
                if word.lower() == word[::-1].lower():
                    palindromes.add(word)
    return palindromes
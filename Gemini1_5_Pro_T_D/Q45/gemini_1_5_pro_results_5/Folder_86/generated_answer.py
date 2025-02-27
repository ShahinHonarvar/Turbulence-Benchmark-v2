import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.findall('[a-zA-Z]', string[6:10])), key=str.casefold)
    result = set()
    if len(letters) >= 4:
        for i in range(4, len(letters) + 1):
            for item in permutations(letters, i):
                word = ''.join(item)
                if word == word[::-1]:
                    result.add(word)
    return result
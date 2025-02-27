import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(re.findall('[a-zA-Z]', text[3:10]))
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters.lower(), i):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 3:
                palindromes.add(word)
    return palindromes
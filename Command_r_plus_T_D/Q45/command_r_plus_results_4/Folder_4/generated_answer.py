import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:10])
    letters = ''.join(letters)
    arrangements = set()
    for i in range(1, len(letters) + 1):
        arrangements.update(set(permutations(letters, i)))
    palindromes = set((arr for arr in arrangements if len(arr) >= 7 and arr == arr[::-1]))
    return palindromes
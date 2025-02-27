import re
    from itertools import permutations

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[5:8])
    lower_letters = ''.join(letters).lower()
    palindromes = set()
    for length in range(4, len(lower_letters) + 1):
        for perm in permutations(lower_letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
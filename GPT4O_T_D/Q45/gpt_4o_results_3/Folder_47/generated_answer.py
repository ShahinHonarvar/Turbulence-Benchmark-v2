from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    sub_str = s[3:8].lower()
    letters = [char for char in sub_str if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        for i in range(5, len(letters) + 1):
            candidate = word[:i]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes
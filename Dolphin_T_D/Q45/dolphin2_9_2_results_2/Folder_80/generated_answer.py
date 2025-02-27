import itertools
    import string

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:9] if char.lower() in string.ascii_lowercase]
    palindromes = set()
    for len_ in range(7, len(letters) + 1):
        for perm in itertools.permutations(letters, len_):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
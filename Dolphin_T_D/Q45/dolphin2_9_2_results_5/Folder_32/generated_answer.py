import itertools, string

def palindromes_between_indices(S):
    palindromes = set()
    english_letters = [char for char in S[1:8] if char in string.ascii_letters]
    for u in range(5, len(english_letters) + 1):
        if len(palindromes) > 0:
            break
        for p in itertools.permutations(english_letters, u):
            word = ''.join(p).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
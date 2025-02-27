import itertools
    import string

def palindromes_between_indices(word):
    word = word[:5].lower() + word[5:]
    word_set = set(word)
    palindromes = {''.join(p) for p in itertools.permutations(word_set) if len(p) >= 4 and p == p[::-1]}
    return palindromes
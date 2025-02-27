import string
    import itertools

def palindromes_between_indices(string):
    assert isinstance(string, str)
    chars = [char for char in string if char in string.ascii_letters]
    if len(chars) < 4:
        return set()
    all_combs = []
    for L in range(4, len(chars) + 1):
        all_combs.extend(list(itertools.permutations(chars, L)))
    palindrome = set()
    for comb in all_combs:
        word = ''.join(comb)
        if word == word.lower() or word == word.upper():
            palindrome.add(word)
    return palindrome
from possible arrangements of English letters in the given string at indices 1 to 4, inclusive.
    import itertools

def palindromes_between_indices(txt):
    """
    Create a set of all palindromes of the length of at least 5 such that each palindrome is created
    """
    text_list = list(txt.lower()[1:5])
    palindromes = set()
    permutations = itertools.permutations(text_list)
    for permutation in permutations:
        if ''.join(permutation) in palindromes or ''.join(permutation[::-1]) in palindromes:
            continue
        if len(''.join(permutation)) >= 5:
            palindromes.add(''.join(permutation))
            palindromes.add(''.join(permutation[::-1]))
    return palindromes
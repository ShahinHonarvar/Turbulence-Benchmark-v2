def palindromes_between_indices(text):
    substring = text[0:9]
    palindromes = set()
    for permutation in itertools.permutations(substring):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 7:
            palindromes.add(palindrome)
    if not palindromes:
        return set()
    return palindromes
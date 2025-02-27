def palindromes_between_indices(text):
    text = text[3:8].lower()
    palindromes = set()
    for permutation in itertools.permutations(text):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes
def palindromes_between_indices(text):
    for i in range(3, 6):
        for permutation in itertools.permutations(text[3:7]):
            palindrome = ''.join(permutation).lower()
            if palindrome != text[3:7].lower():
                palindromes.add(palindrome)
    return palindromes
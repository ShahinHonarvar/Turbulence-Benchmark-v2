def palindromes_between_indices(s):
    letters = set(s.lower()[1:8])
    palindromes = set()
    for length in range(6, 9):
        for combo in itertools.combinations_with_replacement(letters, length):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
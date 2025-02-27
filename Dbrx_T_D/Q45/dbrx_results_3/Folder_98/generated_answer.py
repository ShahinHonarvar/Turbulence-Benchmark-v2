def palindromes_between_indices(s):
    letters = set(s[3:6].lower())
    palindromes = {palindrome for length in range(4, 7) for palindrome in {''.join(pal) for pal in itertools.permutations(letters, length)} if palindrome == palindrome[::-1]}
    return palindromes
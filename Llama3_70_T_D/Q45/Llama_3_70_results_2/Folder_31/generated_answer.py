def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(1, 9) if 'a' <= s[i].lower() <= 'z'))
    palindromes = set()
    for length in range(6, 9 * 2 + 1, 2):
        for first_half in combinations_with_replacement(letters, length // 2):
            palindrome = ''.join(first_half + first_half[::-1])
            palindromes.add(palindrome)
    return palindromes
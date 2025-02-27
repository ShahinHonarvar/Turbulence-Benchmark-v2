def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = set((s[i].lower() for i in range(8) if s[i].lower() in english_letters))
    palindromes = set()
    for p in range(6, 9):
        for combination in combinations(letters_in_range, p):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
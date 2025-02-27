def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = set((s[i].lower() for i in range(5, 10) if s[i].isalpha()))
    if len(letters_in_range) >= 6:
        for perm in permutations(letters_in_range, 6):
            palindrome = ''.join(perm) + ''.join(reversed(perm))
            palindromes.add(palindrome)
    return palindromes
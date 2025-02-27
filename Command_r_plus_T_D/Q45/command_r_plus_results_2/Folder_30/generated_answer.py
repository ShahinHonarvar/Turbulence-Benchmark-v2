def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_range = set((s[i].lower() for i in range(5) if s[i].lower() in english_letters))
    palindromes = set()
    for p in letters_in_range:
        for q in letters_in_range:
            for r in letters_in_range:
                for s_ in letters_in_range:
                    palindrome = p + q + r + s_ + r + q + p
                    palindromes.add(palindrome)
    return palindromes
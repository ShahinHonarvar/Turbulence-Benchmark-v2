def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters_in_range = set((s[i] for i in range(6) if s[i] in english_letters))
    all_palindromes = set()
    for p_length in range(6, len(letters_in_range) + 1):
        for p in combinations(letters_in_range, p_length):
            p_str = ''.join(p)
            if is_palindrome(p_str):
                all_palindromes.add(p_str)
    return all_palindromes
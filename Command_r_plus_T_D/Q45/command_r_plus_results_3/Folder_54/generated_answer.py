def palindromes_between_indices(s: str) -> set[str]:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[4:10].lower()
    english_letters_in_s = set(s_lower).intersection(english_letters)
    palindromes = set()
    for p_length in range(4, len(english_letters_in_s) + 1):
        for p in set((s_lower[i:i + p_length] for i in range(len(s_lower) - p_length + 1))):
            if is_palindrome(p) and set(p) == english_letters_in_s:
                palindromes.add(p)
    return palindromes
def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[:7]
    english_letters = get_english_letters(s)
    all_permutations = set((english_letters[i:j] for i in range(len(english_letters)) for j in range(i + 7, len(english_letters) + 1)))
    palindromes = set((p for p in all_permutations if is_palindrome(p)))
    return palindromes
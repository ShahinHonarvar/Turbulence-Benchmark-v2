def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[:6]
    english_letters = get_english_letters(s)
    all_combinations = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters) + 1):
            all_combinations.update(set(english_letters[i:j]))
    palindromes = set((comb for comb in all_combinations if is_palindrome(comb) and len(comb) >= 6))
    return palindromes
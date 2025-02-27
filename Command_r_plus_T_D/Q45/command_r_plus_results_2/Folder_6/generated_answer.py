def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[:8]
    english_letters = get_english_letters(s)
    unique_letters = set(english_letters)
    palindromes = set()
    for i in range(4, len(english_letters) + 1):
        combinations = set((''.join(p) for p in permutations(english_letters, i)))
        palindromes_at_length_i = {p for p in combinations if is_palindrome(p)}
        palindromes.update(palindromes_at_length_i)
    return palindromes
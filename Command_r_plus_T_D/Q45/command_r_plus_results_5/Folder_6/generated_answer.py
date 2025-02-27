def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[:8]
    english_letters = get_english_letters(s)
    all_palindromes = set()
    for i in range(1, len(english_letters)):
        for window in zip(*[english_letters[j:] for j in range(i)]):
            window_str = ''.join(window)
            if is_palindrome(window_str) and len(window_str) >= 4:
                all_palindromes.add(window_str)
    return all_palindromes
def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[:4]
    english_letters = get_english_letters(s)
    all_palindromes = set()
    for i in range(1, len(english_letters) + 1):
        for perm in permutations(english_letters, i):
            word = ''.join(perm)
            if is_palindrome(word) and len(word) >= 4:
                all_palindromes.add(word)
    return all_palindromes
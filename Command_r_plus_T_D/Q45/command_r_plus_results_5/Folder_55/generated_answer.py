def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[:3])
    palindromes = set()
    for i in range(1, len(english_letters) + 1):
        for perm in set(itertools.permutations(english_letters, i)):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes
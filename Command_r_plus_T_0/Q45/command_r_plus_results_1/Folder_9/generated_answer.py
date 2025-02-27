def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    s = s[:7]
    english_letters = get_english_letters(s)
    all_permutations = set(itertools.permutations(english_letters))
    palindromes = {p for p in all_permutations if is_palindrome(''.join(p))}
    return {p for p in palindromes if len(p) >= 7}
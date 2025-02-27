def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def is_english_letter(char: str) -> bool:
        return char.isalpha()
    english_letters = [char.lower() for char in s[1:9] if is_english_letter(char)]
    all_possible_palindromes = set()
    for i in range(6, len(english_letters) + 1):
        possible_palindromes = set((''.join(p) for p in permutations(english_letters, i) if is_palindrome(p)))
        all_possible_palindromes.update(possible_palindromes)
    return all_possible_palindromes
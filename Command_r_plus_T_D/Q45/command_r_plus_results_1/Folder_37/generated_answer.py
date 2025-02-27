def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join(filter(str.isalpha, s)).lower()
    s = s[1:5]
    english_letters = get_english_letters(s)
    all_combinations = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters) + 1):
            all_combinations.add(english_letters[i:j])
    return set(filter(is_palindrome, all_combinations))
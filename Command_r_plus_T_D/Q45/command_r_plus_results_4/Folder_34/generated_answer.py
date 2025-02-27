def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(string: str) -> str:
        return ''.join((char for char in string if char.isalpha()))
    palindromes = set()
    for i in range(5, 8):
        for j in range(i + 1, 8):
            substring = get_english_letters(input_string[i:j]).lower()
            if len(substring) >= 4 and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes
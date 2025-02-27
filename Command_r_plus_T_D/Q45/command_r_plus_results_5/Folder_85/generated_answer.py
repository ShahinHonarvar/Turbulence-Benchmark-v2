def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    input_string = input_string.lower()
    possible_palindromes = set()
    for i in range(2, 9):
        for j in range(i + 1, 9):
            substring = input_string[i:j]
            if all((char in english_letters for char in substring)):
                if is_palindrome(substring) and len(substring) >= 7:
                    possible_palindromes.add(substring)
    return possible_palindromes
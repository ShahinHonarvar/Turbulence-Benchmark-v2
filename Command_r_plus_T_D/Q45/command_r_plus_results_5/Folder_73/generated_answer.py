def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    english_letters = ''.join(filter(str.isalpha, s[3:7].lower()))
    all_palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 3, len(english_letters) + 1):
            substring = english_letters[i:j]
            if is_palindrome(substring):
                all_palindromes.add(substring)
    return all_palindromes
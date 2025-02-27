def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    substring = input_string[3:9]
    for p in substring:
        if p in english_letters:
            substring_letters_only = ''.join(filter(lambda x: x in english_letters, substring))
            if len(substring_letters_only) >= 7 and is_palindrome(substring_letters_only):
                palindromes.add(substring_letters_only)
    return palindromes
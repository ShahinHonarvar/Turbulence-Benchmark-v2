def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr[::-1].lower()

    def only_letters(substr):
        return ''.join(filter(str.isalpha, substr))
    result = set()
    limited_string = s[:21]
    for start in range(len(limited_string)):
        for end in range(start + 5, len(limited_string) + 1):
            if end - start > 80:
                break
            substring = limited_string[start:end]
            letter_only_substring = only_letters(substring)
            if 5 <= len(letter_only_substring) <= 80 and is_palindrome(letter_only_substring):
                result.add(letter_only_substring)
    return result
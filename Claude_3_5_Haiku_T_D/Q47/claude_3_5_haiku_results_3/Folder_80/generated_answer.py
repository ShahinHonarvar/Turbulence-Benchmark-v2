def palindromes_of_specific_lengths(s):

    def is_palindrome(string):
        return string == string[::-1]

    def contains_only_english_letters(string):
        return all((char.isalpha() for char in string))
    result = set()
    for length in range(24, 34):
        for start in range(35, 89 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and contains_only_english_letters(substring):
                result.add(substring)
    return result
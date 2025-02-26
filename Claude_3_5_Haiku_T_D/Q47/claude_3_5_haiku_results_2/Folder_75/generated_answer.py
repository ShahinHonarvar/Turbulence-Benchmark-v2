def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_all_letters(word):
        return word.isalpha()
    palindrome_set = set()
    for length in range(23, 40):
        for start in range(31, 75 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_all_letters(substring):
                palindrome_set.add(substring)
    return palindrome_set
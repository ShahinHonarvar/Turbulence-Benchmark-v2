def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_only_letters(word):
        return word.isalpha()
    palindrome_set = set()
    for length in range(40, 48):
        for i in range(45, 99 - length + 1):
            substr = s[i:i + length].lower()
            if is_palindrome(substr) and is_only_letters(substr):
                palindrome_set.add(substr)
    return palindrome_set
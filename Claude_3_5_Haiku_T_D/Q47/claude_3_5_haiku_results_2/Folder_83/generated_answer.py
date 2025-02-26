def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_letters_only(word):
        return word.isalpha()
    palindromes = set()
    substring = s[75:96]
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if is_palindrome(candidate) and is_letters_only(candidate):
                palindromes.add(candidate)
    return palindromes
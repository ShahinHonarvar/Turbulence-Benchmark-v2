def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_alphabetic(word):
        return word.isalpha()
    palindromes = set()
    substring = s[130:296].lower()
    for length in range(103, 159):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and is_alphabetic(candidate):
                palindromes.add(candidate)
    return palindromes
def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_only_letters(word):
        return word.isalpha()
    palindromes = set()
    substring = s[36:93]
    for length in range(10, 36):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if is_palindrome(candidate) and is_only_letters(candidate):
                palindromes.add(candidate)
    return palindromes
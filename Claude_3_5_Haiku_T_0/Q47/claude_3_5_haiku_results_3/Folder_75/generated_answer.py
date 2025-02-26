def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_only_letters(word):
        return word.isalpha()
    palindromes = set()
    substring = s[31:75].lower()
    for length in range(23, 40):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_only_letters(candidate):
                palindromes.add(candidate)
    return palindromes
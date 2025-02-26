def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_letters_only(word):
        return word.isalpha()
    palindromes = set()
    if len(s) < 91:
        return palindromes
    substring = s[14:91]
    for length in range(55, 72):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if is_palindrome(candidate) and is_letters_only(candidate):
                palindromes.add(candidate)
    return palindromes
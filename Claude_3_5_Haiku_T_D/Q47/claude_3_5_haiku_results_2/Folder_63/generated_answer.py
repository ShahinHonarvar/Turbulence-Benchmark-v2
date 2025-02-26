def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_only_letters(word):
        return word.isalpha()
    palindromes = set()
    substring = s[33:86]
    for length in range(26, 32):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length].lower()
            if is_palindrome(potential_palindrome) and is_only_letters(potential_palindrome):
                palindromes.add(potential_palindrome)
    return palindromes
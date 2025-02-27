def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    substring = s[:11].lower()
    for length in range(3, 6):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word.isalpha() and is_palindrome(word):
                palindromes.add(word)
    return palindromes
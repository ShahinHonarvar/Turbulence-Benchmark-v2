def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    substring = s[18:66]
    palindromes = set()
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes
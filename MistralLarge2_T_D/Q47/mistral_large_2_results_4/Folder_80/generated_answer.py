def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[35:89].lower()
    palindromes = set()
    for length in range(24, 34):
        for i in range(len(substring) - length + 1):
            sub_palindrome = substring[i:i + length]
            if is_palindrome(sub_palindrome) and sub_palindrome.isalpha():
                palindromes.add(sub_palindrome)
    return palindromes
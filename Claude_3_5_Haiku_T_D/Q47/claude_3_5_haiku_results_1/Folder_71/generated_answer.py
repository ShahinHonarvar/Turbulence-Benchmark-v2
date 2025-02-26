def palindromes_of_specific_lengths(s):

    def is_palindrome(string):
        return string == string[::-1]

    def is_english_letters(string):
        return string.isalpha()
    palindromes = set()
    s_slice = s[18:66].lower()
    for length in range(23, 37):
        for start in range(len(s_slice) - length + 1):
            substring = s_slice[start:start + length]
            if is_palindrome(substring) and is_english_letters(substring):
                palindromes.add(substring)
    return palindromes
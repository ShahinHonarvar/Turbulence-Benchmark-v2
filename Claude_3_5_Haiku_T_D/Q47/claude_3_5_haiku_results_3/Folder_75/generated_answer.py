def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    substring = s[31:75]
    for length in range(23, 40):
        for start in range(len(substring) - length + 1):
            current_substring = substring[start:start + length]
            if is_palindrome(current_substring) and is_only_letters(current_substring):
                palindromes.add(current_substring.lower())
    return palindromes
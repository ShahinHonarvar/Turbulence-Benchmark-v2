def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    start_index = 22
    end_index = 95
    for length in range(52, 56):
        for i in range(start_index, end_index - length + 2):
            substring = s[i:i + length]
            if is_palindrome(substring) and is_only_letters(substring):
                palindromes.add(substring.lower())
    return palindromes
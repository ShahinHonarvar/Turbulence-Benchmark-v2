def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    palindromes = set()
    for start in range(11, 94):
        for length in range(34, 55):
            end = start + length
            if end <= len(s):
                substring = s[start:end]
                if is_palindrome(substring) and is_only_letters(substring):
                    palindromes.add(substring)
    return palindromes
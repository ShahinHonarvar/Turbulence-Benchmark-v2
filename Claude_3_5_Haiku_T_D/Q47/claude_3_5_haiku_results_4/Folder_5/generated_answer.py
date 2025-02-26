def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_only_letters(substring):
        return substring.isalpha()
    if len(s) < 71:
        return set()
    substring = s[63:71]
    palindromes = set()
    for start in range(len(substring)):
        for length in range(4, 6):
            if start + length <= len(substring):
                candidate = substring[start:start + length]
                if is_palindrome(candidate) and is_only_letters(candidate):
                    palindromes.add(candidate.lower())
    return palindromes
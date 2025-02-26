def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def contains_only_letters(substring):
        return substring.isalpha()
    palindrome_set = set()
    if len(s) < 96:
        return palindrome_set
    substring = s[75:96].lower()
    for length in range(7, 10):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and contains_only_letters(candidate):
                palindrome_set.add(candidate)
    return palindrome_set
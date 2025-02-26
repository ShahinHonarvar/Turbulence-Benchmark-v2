def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def is_alpha_only(substring):
        return substring.isalpha()
    palindrome_set = set()
    if len(s) < 201:
        return palindrome_set
    substring = s[100:201].lower()
    for length in range(5, 11):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_alpha_only(candidate):
                palindrome_set.add(candidate)
    return palindrome_set
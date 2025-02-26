def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_alpha_only(word):
        return word.isalpha()
    s = s.lower()
    palindrome_set = set()
    for length in range(52, 57):
        for start in range(26, 88 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_alpha_only(substring):
                palindrome_set.add(substring)
    return palindrome_set
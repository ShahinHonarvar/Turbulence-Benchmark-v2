def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_alpha_only(word):
        return word.isalpha()
    palindrome_set = set()
    if len(s) < 301:
        return palindrome_set
    substring = s[200:301].lower()
    for length in range(10, 51):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_alpha_only(candidate):
                palindrome_set.add(candidate)
    return palindrome_set
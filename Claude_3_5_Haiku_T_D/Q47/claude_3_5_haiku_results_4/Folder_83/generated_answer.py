def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    if len(s) < 96:
        return set()
    substring = s[75:96].lower()
    palindrome_set = set()
    for length in range(7, 10):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_only_letters(candidate):
                palindrome_set.add(candidate)
    return palindrome_set
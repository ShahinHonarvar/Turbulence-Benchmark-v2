def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]

    def is_letter_only(x):
        return x.isalpha()
    palindromes = set()
    substring = s[18:99].lower()
    for length in range(31, 52):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_letter_only(candidate):
                palindromes.add(candidate)
    return palindromes
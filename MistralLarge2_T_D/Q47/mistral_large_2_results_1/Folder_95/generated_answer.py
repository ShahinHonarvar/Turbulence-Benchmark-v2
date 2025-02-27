def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    substring = s[12:57].lower()
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes
def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    palindromes = set()
    s = ''.join(filter(str.isalpha, s[20:75])).lower()
    for length in range(36, 43):
        for i in range(len(s) - length + 1):
            candidate = s[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes
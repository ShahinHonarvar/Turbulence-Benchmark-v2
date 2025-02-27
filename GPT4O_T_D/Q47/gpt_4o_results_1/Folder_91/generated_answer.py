def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = ''.join(filter(str.isalpha, s[:11])).lower()
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes
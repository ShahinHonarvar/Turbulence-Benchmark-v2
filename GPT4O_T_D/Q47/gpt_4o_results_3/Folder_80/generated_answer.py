def palindromes_of_specific_lengths(s):
    filtered_substring = ''.join(filter(str.isalpha, s[35:89])).lower()
    palindromes = set()
    n = len(filtered_substring)

    def is_palindrome(sub):
        return sub == sub[::-1]
    for length in range(24, 34):
        for i in range(n - length + 1):
            candidate = filtered_substring[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(s[35:89][i:i + length])
    return palindromes
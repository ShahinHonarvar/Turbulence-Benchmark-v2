def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    valid_substring = s[26:88]
    palindromes = set()
    for length in range(52, 57):
        for start in range(len(valid_substring) - length + 1):
            sub = valid_substring[start:start + length]
            filtered_sub = ''.join((c for c in sub if c.isalpha())).lower()
            if len(filtered_sub) == length and is_palindrome(filtered_sub):
                palindromes.add(filtered_sub)
    return palindromes
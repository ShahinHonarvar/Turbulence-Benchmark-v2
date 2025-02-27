def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[15:95]
    palindromes = set()
    for length in range(18, 74):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            filtered_sub = ''.join((c.lower() for c in sub if c.isalpha()))
            if len(filtered_sub) == length and is_palindrome(filtered_sub):
                palindromes.add(filtered_sub)
    return palindromes
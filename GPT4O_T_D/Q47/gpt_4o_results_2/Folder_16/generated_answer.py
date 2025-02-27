def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = sub.lower()
        return sub == sub[::-1]
    s = s[15:87]
    palindromes = set()
    for length in range(51, 61):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            letters_only = ''.join(filter(str.isalpha, substr))
            if len(letters_only) == length and is_palindrome(letters_only):
                palindromes.add(letters_only)
    return palindromes
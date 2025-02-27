def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = ''.join(filter(str.isalpha, s[18:66]))
    palindromes = set()
    lengths = range(23, 37)
    for length in lengths:
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes
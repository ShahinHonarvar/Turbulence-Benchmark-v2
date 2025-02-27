def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[12:57]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(s) - length + 1):
            if is_palindrome(s[i:i + length]):
                palindromes.add(s[i:i + length])
    return palindromes
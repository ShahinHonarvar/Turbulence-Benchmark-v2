def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    for length in range(3, 6):
        for i in range(11 - length + 1):
            sub = s[i:i + length].lower()
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes
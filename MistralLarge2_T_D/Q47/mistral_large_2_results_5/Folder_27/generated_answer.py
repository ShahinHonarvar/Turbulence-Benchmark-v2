def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    substring = s[13:100].lower()
    for length in range(26, 30):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes
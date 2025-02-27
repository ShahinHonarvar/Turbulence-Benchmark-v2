def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[1:8].lower()
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes
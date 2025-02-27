def palindromes_of_specific_lengths(s):

    def is_palindrome(sub, length):
        return sub[:length] == sub[:length][::-1]
    s = s[12:123].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(12, 221):
            if i + j <= len(s) and is_palindrome(s[i:i + j], j) and s[i:i + j].isalpha():
                palindromes.add(s[i:i + j])
    return palindromes
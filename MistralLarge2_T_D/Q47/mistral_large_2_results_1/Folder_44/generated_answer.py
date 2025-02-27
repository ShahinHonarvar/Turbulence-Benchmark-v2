def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[18:99]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(31, 52):
            if i + j <= len(substring):
                sub = substring[i:i + j]
                if sub.isalpha() and is_palindrome(sub.lower()):
                    palindromes.add(sub.lower())
    return palindromes
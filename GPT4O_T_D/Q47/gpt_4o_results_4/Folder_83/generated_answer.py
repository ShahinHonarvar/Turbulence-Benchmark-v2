def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = ''.join((char for char in s[75:96] if char.isalpha())).lower()
    palindromes = set()
    for i in range(len(substring)):
        for length in range(7, 10):
            if i + length <= len(substring):
                sub = substring[i:i + length]
                if is_palindrome(sub):
                    palindromes.add(sub)
    return palindromes
from string import ascii_letters

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[127:289].lower()
    palindromes = set()
    for length in range(119, 142):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((c in ascii_letters for c in sub)) and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes
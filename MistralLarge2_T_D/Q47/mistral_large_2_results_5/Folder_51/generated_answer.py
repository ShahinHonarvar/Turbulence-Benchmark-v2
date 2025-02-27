def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[2:9]
    palindromes = set()
    length = len(substring)
    for i in range(length - 2):
        for j in range(3, 5):
            if i + j <= length:
                sub = substring[i:i + j]
                if sub.isalpha() and is_palindrome(sub.lower()):
                    palindromes.add(sub)
    return palindromes
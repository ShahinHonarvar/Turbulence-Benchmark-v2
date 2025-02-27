def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[18:66]
    palindromes = set()
    length = len(substring)
    for i in range(length):
        for j in range(23, 37):
            if i + j <= length:
                candidate = substring[i:i + j]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate)
    return palindromes
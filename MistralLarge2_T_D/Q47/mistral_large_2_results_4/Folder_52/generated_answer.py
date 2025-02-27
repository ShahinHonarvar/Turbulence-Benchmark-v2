def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[44:100].lower()
    palindromes = set()
    length = len(substring)
    for i in range(length):
        for j in range(i + 13, min(i + 43, length) + 1):
            if j - i >= 13 and j - i <= 42:
                candidate = substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes
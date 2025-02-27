def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[2:4].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            candidate = substring[i:j]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes
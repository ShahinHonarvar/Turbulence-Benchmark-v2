def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = ''.join([c for c in sub if c.isalpha()]).lower()
        return sub == sub[::-1]
    valid_palindromes = set()
    substring = s[44:100]
    for start in range(len(substring)):
        for end in range(start + 13, min(start + 43, len(substring) + 1)):
            candidate = substring[start:end]
            if is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes
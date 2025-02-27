def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = ''.join((c for c in sub if c.isalpha())).lower()
        return sub == sub[::-1]
    result = set()
    substring = s[40:95]
    for start in range(len(substring)):
        for length in range(45, 52):
            end = start + length
            if end <= len(substring):
                candidate = substring[start:end]
                if is_palindrome(candidate):
                    pure_letters = ''.join((c for c in candidate if c.isalpha()))
                    result.add(pure_letters)
    return result
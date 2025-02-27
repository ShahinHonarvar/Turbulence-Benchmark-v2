def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    result = set()
    substring = s[17:96].lower()
    for start in range(len(substring)):
        for length in range(13, 50):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if all((c.isalpha() for c in candidate)) and is_palindrome(candidate):
                result.add(candidate)
    return result
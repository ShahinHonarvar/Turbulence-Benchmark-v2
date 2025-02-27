def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = s[27:78]
    substr_filtered = ''.join([c for c in substr if c in valid_chars]).lower()
    results = set()
    for length in range(18, 20):
        for start in range(len(substr_filtered) - length + 1):
            candidate = substr_filtered[start:start + length]
            if is_palindrome(candidate):
                results.add(candidate)
    return results
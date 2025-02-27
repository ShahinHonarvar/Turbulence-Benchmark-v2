def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[27:96].lower()
    results = set()
    for length in range(49, 52):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                results.add(sub)
    return results
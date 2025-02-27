def palindromes_of_specific_lengths(s):
    s = s[17:73].lower()
    result = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for length in range(50, 52):
        for start in range(len(s) - length + 1):
            candidate = s[start:start + length]
            filtered = ''.join((c for c in candidate if c.isalpha()))
            if len(filtered) == length and is_palindrome(filtered):
                result.add(candidate)
    return result
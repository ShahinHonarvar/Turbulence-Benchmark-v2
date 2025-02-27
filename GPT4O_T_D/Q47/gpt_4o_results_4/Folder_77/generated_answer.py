def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = sub.lower()
        return sub == sub[::-1]
    substring = s[103:277]
    length_range = range(100, 170)
    palindromes_set = set()
    for length in length_range:
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((c.isalpha() for c in candidate)) and is_palindrome(candidate):
                palindromes_set.add(candidate)
    return palindromes_set
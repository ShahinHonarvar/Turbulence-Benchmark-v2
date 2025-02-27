def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    filtered_substr = ''.join([c for c in s[35:89] if c.isalpha()]).lower()
    result = set()
    for length in range(24, 34):
        for start in range(len(filtered_substr) - length + 1):
            sub = filtered_substr[start:start + length]
            if is_palindrome(sub):
                result.add(sub)
    return result
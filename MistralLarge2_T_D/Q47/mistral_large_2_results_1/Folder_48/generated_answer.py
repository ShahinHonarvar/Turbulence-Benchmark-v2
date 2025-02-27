def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substr = s[155:284].lower()
    result = set()
    for length in range(104, 121):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result
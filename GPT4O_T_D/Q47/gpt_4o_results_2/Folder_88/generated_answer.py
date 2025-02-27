def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = ''.join((c for c in sub if c.isalpha())).lower()
        return sub == sub[::-1]
    result = set()
    lower_bound = 11
    upper_bound = 87
    s = s[lower_bound:upper_bound + 1]
    for i in range(len(s)):
        for length in range(4, 6):
            if i + length <= len(s):
                potential_palindrome = s[i:i + length]
                if is_palindrome(potential_palindrome):
                    result.add(potential_palindrome.lower())
    return result
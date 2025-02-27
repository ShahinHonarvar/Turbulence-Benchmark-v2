def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub.lower()))
        return sub == sub[::-1]
    result = set()
    sub_s = s[10:60]
    for length in range(18, 37):
        for start in range(len(sub_s) - length + 1):
            candidate = sub_s[start:start + length]
            if is_palindrome(candidate):
                result.add(''.join(filter(str.isalpha, candidate.lower())))
    return result
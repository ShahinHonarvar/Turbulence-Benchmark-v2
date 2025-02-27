def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    sub_str = ''.join([c.lower() for c in s[12:93] if c.isalpha()])
    for i in range(len(sub_str)):
        for length in range(42, 78):
            if i + length <= len(sub_str):
                candidate = sub_str[i:i + length]
                if is_palindrome(candidate):
                    result.add(candidate)
    return result
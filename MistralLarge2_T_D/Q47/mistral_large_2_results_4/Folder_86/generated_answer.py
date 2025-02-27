def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    sub_string = s[30:96].lower()
    for length in range(34, 56):
        for start in range(len(sub_string) - length + 1):
            sub = sub_string[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result
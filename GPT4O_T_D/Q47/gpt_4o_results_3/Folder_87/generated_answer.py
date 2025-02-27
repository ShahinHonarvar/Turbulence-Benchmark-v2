def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s_sub = ''.join(filter(str.isalpha, s[11:94]))
    result = set()
    for length in range(34, 55):
        for i in range(len(s_sub) - length + 1):
            substr = s_sub[i:i + length]
            if is_palindrome(substr):
                result.add(substr)
    return result
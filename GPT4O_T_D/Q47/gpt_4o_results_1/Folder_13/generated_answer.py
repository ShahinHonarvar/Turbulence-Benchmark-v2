def palindromes_of_specific_lengths(s):

    def is_palindrome(start, end):
        substring = s[start:end + 1].lower()
        return substring == substring[::-1]
    s = ''.join([c for c in s[13:96] if c.isalpha()])
    palins = set()
    for length in range(57, 61):
        for i in range(len(s) - length + 1):
            if is_palindrome(i, i + length - 1):
                palins.add(s[i:i + length])
    return palins
def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    res = set()
    for i in range(len(s) - 28):
        for j in range(i + 29, len(s) + 1):
            res.add(s[i:j])
    return {word for word in res if is_palindrome(word) and len(word) >= 29}
def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]
    s_len = len(s)
    result = set()
    for i in range(s_len):
        for j in range(i + 52, s_len + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result
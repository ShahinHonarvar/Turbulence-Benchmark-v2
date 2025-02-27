def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    n = 96
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for start in range(len(s)):
        for end in range(start + n, len(s) + 1):
            if is_palindrome(s[start:end]):
                result.add(s[start:end])
    return result
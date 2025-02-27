def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(s) < 36:
        return set()
    result = set()
    for start in range(len(s)):
        for end in range(start + 36, len(s) + 1):
            if is_palindrome(s[start:end]):
                result.add(s[start:end])
    return result
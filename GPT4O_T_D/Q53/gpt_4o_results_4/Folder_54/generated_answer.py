def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    results = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 74, length + 1):
            if is_palindrome(s[i:j]):
                results.add(s[i:j])
    return results
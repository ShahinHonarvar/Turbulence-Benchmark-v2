def palindrome_of_length_at_least_n(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    results = set()
    n = 87
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                results.add(substring)
    return results
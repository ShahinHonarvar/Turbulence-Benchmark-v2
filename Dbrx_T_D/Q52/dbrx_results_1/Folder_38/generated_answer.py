def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    if n < 38:
        return set()

    def is_palindrome(substring):
        i, j = (0, len(substring) - 1)
        while i < j:
            if substring[i] != substring[j]:
                return False
            i += 1
            j -= 1
        return True
    result = set()
    for i in range(n - 36):
        for j in range(n - 38 + i, n - i):
            substring = s[i:j + 1]
            if is_palindrome(substring):
                result.add(substring)
    return result
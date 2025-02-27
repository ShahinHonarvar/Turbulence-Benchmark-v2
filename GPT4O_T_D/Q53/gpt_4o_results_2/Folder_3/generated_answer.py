def palindrome_of_length_at_least_n(s):

    def is_palindrome(start, end):
        while start < end:
            if filtered[start] != filtered[end]:
                return False
            start += 1
            end -= 1
        return True
    s = s.lower()
    filtered = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    length = len(filtered)
    for i in range(length):
        for j in range(i + 58, length):
            if is_palindrome(i, j):
                palindromes.add(filtered[i:j + 1])
    return palindromes
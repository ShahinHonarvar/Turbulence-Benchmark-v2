def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(length, i, -1):
            if j - i + 1 < 90:
                break
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
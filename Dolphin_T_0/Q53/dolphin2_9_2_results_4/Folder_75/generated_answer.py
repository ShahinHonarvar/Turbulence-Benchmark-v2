def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 1, length):
            if s[i:j + 1] == s[i:j + 1][::-1] and len(s[i:j + 1]) >= 40:
                palindromes.add(s[i:j + 1])
    return palindromes
def palindrome_of_length_at_least_n(s):
    palindromeSet = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 89, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and set(substring) <= set('abcdefghijklmnopqrstuvwxyz'):
                palindromeSet.add(substring)
    return palindromeSet
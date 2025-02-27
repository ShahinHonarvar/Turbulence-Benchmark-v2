def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 39):
        for j in range(i, len(s) - i):
            if j + 40 > len(s):
                break
            substring = s[j:j + 40]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
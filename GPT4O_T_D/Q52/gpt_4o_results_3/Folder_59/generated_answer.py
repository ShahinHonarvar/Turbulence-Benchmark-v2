def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindrome_set = set()
    n = 39
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set
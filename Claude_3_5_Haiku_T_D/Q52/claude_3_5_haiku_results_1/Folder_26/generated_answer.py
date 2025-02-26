def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 365):
        substring = s[i:i + 366]
        if len(substring) == 366 and substring == substring[::-1] and substring.isalpha():
            palindrome_set.add(substring)
    return palindrome_set
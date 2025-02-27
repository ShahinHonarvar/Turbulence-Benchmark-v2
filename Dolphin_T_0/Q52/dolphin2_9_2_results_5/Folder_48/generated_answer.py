def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    for i in range(len(s) - 185):
        temp = s[i:i + 186]
        if temp == temp[::-1] and all((c.isalpha() for c in temp)):
            palindrome_set.add(temp)
    return palindrome_set
def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 71):
        sub = s[i:i + 72]
        if sub == sub[::-1]:
            result.add(''.join(filter(str.isalpha, sub.lower())))
    return result
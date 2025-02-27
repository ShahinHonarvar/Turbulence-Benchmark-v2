def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()
    for i in range(n - 82):
        substring = s[i:i + 83]
        if substring == substring[::-1]:
            result.add(s[i:i + 83])
    return result
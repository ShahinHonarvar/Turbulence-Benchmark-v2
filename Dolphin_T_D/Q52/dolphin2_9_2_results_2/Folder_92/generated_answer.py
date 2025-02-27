def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 9):
        if s[i:i + 10] == s[i:i + 10][::-1]:
            result.add(s[i:i + 10])
    return result
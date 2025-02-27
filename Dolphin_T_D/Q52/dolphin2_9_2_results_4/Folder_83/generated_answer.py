def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 23):
        temp = s[i:i + 24]
        if temp == temp[::-1]:
            result.add(temp)
    return result
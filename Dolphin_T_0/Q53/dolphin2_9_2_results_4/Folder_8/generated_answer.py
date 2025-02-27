def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(length, 0, -1):
            temp = s[i:j]
            if len(temp) >= 45 and temp == temp[::-1]:
                result.add(temp)
    return result
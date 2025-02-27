def palindrome_of_length_n(s):
    result = set()
    n = 45
    for i in range(len(s) - n + 1):
        temp = s[i:i + n]
        if temp == temp[::-1]:
            result.add(temp)
    return result
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 14
    result = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            temp = s[i:j]
            if temp == temp[::-1] and temp.isalpha():
                result.add(temp)
    return result
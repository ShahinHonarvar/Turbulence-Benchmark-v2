def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]
            temp = temp.lower()
            if temp == temp[::-1] and len(temp) >= 41:
                result.add(temp)
    return result
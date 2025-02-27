def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 66):
        for j in range(i + 67, len(s)):
            temp = s[i:j + 1]
            if temp == temp[::-1]:
                result.add(temp.lower())
    return result
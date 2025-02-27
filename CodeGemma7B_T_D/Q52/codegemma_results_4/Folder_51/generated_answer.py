def palindrome_of_length_n(str1):
    result = set()
    for i in range(len(str1)):
        for j in range(i + 72, len(str1)):
            s = str1[i:j + 1]
            if s == s[::-1] and s.isalpha():
                result.add(s.lower())
    return result
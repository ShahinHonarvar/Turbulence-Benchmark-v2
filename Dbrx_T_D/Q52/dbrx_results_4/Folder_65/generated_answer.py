def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 34):
        for j in range(i, i + 35):
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha():
                result.add(s[i:j + 1])
    return result
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 54):
        for j in range(i, len(s) - i):
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha():
                result.add(s[i:j + 1])
    return result
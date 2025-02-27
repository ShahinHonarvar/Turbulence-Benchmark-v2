def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 20):
        for j in range(i, i + 21):
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha():
                result.add(s[i:j + 1])
    return result
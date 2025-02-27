def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 33):
        for j in range(i + 1, i + 35):
            if s[i:j] == s[j:i:-1]:
                result.add(s[i:j])
    return result
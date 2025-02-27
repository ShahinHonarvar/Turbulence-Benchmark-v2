def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    result_set = set()
    for i in range(length):
        for j in range(i + 25, length):
            if s[i:j] == s[i:j][::-1]:
                result_set.add(s[i:j])
    return result_set
def palindrome_of_length_n(s):
    result_set = set()
    s = s.lower()
    for i in range(len(s) - 186):
        for j in range(186):
            if s[i + j] != s[i + 186 - j - 1]:
                break
            elif j == 185:
                result_set.add(s[i:i + 187])
    return result_set
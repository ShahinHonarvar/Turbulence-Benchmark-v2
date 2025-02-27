def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 17):
        sub_s = s[i:i + 18]
        if sub_s == sub_s[::-1] and sub_s.isalpha():
            result.add(sub_s)
    return result
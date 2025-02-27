def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 94):
        sub_s = s[i:i + 95]
        if sub_s == sub_s[::-1]:
            result.add(sub_s)
    return result
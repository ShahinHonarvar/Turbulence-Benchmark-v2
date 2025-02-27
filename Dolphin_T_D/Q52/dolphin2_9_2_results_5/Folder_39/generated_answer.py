def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s) - 58):
        sub_s = s[i:i + 59]
        if sub_s == sub_s[::-1] and sub_s.isalpha():
            result_set.add(sub_s)
    return result_set
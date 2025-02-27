def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        if i + 338 <= len(s):
            sub_s = s[i:i + 338]
            if sub_s == sub_s[::-1]:
                result.add(sub_s)
    return result
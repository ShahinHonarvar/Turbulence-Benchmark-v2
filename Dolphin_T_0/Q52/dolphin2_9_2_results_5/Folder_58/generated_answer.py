def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 223, len(s) + 1):
            sub_s = s[i:j]
            if sub_s == sub_s[::-1] and len(sub_s) == 223 and all((c.isalpha() for c in sub_s)):
                result.add(sub_s)
    return result
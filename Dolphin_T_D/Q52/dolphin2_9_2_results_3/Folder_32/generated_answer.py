def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 112):
        for p in range(i + 1, i + 114):
            if s[i:p] == s[i:p][::-1] and len(s[i:p]) == 113:
                result.add(s[i:p].upper())
    return result
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 94):
        if s[i:i + 95] == s[i:i + 95][::-1]:
            result.add(s[i:i + 95])
    return result
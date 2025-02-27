def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 92):
        if s[i:i + 93] == s[i:i + 93][::-1]:
            result.add(s[i:i + 93])
    return result
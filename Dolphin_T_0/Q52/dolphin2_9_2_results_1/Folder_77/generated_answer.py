def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 172):
        if s[i:i + 173] == s[i:i + 173][::-1]:
            result.add(s[i:i + 173])
    return result
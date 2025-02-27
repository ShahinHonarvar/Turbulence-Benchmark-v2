def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 172):
        if s[i:i + 173] == s[i:i + 173][::-1]:
            result.add(s[i:i + 173])
    return result
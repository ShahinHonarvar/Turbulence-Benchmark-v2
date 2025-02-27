def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 56):
        if s[i:i + 57] == s[i:i + 57][::-1] and s[i:i + 57].isalpha():
            result.add(s[i:i + 57])
    return result
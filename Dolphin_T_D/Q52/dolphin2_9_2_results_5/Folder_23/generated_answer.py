def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 68):
        part = s[i:i + 69]
        if part == part[::-1] and part.isalpha():
            result.add(part)
    return result
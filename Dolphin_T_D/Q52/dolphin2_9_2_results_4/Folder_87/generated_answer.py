def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 57, len(s) + 1):
            if s[i:j].isalpha() and s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result
def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.replace(' ', '')
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 77, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                result.add(s[i:j + 1])
    return result
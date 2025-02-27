def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 21):
        for j in range(i + 11, len(s)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result
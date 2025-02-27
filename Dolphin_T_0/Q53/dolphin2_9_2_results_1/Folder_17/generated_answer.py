def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 35):
        for length in range(36, len(s) - i + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                result.add(s[i:i + length])
    return result
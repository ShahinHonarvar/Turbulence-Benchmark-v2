def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        if i + 41 <= len(s):
            sub = s[i:i + 41]
            if sub == sub[::-1]:
                result.add(sub)
    return result
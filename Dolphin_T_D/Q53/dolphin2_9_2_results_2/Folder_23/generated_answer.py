def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        if i + 19 <= len(s):
            sub = s[i:i + 20]
            if sub == sub[::-1]:
                result.add(sub)
        else:
            break
    return result
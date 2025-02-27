def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 52, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result
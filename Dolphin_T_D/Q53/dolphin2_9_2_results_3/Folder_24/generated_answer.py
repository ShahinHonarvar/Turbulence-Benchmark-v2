def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 53, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result
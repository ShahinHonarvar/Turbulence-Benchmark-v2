def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 32, len(s)):
            sub = s[i:j + 1].lower()
            if sub == sub[::-1]:
                result.add(sub)
    return result
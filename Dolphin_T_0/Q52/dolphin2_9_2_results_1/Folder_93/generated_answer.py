def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 45, len(s) + 1):
            sub = s[i:j].lower()
            if sub == sub[::-1]:
                result.add(sub)
    return result
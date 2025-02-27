def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 11, len(s) + 1):
            if s[i].lower() == s[j - 1].lower():
                substring = s[i:j]
                if substring == substring[::-1]:
                    result.add(substring)
    return result
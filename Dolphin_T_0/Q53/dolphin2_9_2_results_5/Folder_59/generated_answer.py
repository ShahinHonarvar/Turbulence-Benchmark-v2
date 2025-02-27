def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1]
            if len(substring) >= 20 and substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
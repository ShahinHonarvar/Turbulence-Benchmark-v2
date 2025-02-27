def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 140):
        for j in range(i + 140, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result
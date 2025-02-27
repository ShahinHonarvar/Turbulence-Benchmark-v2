def palindrome_of_length_n(s):
    results = set()
    for i in range(len(s)):
        for j in range(i + 68, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                results.add(substring.lower())
    return results
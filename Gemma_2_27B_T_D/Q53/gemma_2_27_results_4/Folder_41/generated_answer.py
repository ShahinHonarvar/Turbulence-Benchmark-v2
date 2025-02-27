def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s) - 27):
        for j in range(i + 27, len(s) + 1):
            substring = s[i:j]
            if substring.lower() == substring.lower()[::-1] and len(substring) >= 28:
                result.add(substring)
    return result
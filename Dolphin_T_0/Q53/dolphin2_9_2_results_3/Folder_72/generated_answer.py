def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(88, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            if s[j:j + i].lower() == s[j:j + i].lower()[::-1]:
                result.add(s[j:j + i])
    return result
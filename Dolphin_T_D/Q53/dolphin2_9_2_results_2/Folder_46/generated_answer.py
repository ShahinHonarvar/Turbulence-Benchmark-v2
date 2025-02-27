def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s)):
        for j in range(i + 85, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                result_set.add(substring)
    return result_set
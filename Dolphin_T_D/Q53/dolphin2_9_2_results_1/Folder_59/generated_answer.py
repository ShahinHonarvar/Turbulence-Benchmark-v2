def palindrome_of_length_at_least_n(s):
    result = set()
    for length in range(20, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                result.add(sub.lower())
    return result
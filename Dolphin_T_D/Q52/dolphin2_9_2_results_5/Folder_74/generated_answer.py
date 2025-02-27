def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 95):
        candidate = s[i:i + 96]
        if candidate == candidate[::-1]:
            result.add(candidate)
    return result
def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 29):
        for j in range(i + 30, len(s) + 1):
            segment = s[i:j]
            if segment == segment[::-1]:
                result.add(segment)
    return result
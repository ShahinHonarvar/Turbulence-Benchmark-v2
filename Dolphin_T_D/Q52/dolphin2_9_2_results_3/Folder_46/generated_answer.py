def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        if i + 464 <= len(s):
            candidate = s[i:i + 464]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result
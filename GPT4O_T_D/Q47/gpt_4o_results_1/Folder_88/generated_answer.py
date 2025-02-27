def palindromes_of_specific_lengths(s):
    s = s[11:88]
    result = set()
    for i in range(len(s)):
        for length in range(4, 6):
            if i + length <= len(s):
                substring = s[i:i + length]
                alphanumeric = ''.join((ch.lower() for ch in substring if ch.isalpha()))
                if alphanumeric == alphanumeric[::-1] and len(alphanumeric) == length:
                    result.add(alphanumeric)
    return result
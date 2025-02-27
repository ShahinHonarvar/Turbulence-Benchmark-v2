def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        if ''.join(reversed(substring)) == substring:
            result.add(substring)
    return result
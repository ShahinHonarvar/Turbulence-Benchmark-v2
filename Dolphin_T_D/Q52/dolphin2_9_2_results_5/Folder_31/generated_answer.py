def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 64):
        substring = s[i:i + 66]
        if substring == substring[::-1]:
            result.add(substring)
    return result
def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 67):
        substring = s[i:i + 68].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result
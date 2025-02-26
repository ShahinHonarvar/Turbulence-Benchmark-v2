def palindrome_of_length_n(s):
    s = ''.join((char.lower() for char in s if char.isalpha()))
    result = set()
    for i in range(len(s) - 45):
        substring = s[i:i + 46]
        if substring == substring[::-1]:
            result.add(substring)
    return result
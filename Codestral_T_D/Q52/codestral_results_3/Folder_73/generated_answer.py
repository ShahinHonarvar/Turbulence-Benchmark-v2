def palindrome_of_length_n(s):
    length = 41
    result = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result
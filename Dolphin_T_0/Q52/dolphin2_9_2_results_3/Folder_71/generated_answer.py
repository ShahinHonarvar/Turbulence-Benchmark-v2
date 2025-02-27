def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 77):
        substring = s[i:i + 78]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result
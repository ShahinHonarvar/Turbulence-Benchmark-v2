def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 463):
        substring = s[i:i + 464].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result
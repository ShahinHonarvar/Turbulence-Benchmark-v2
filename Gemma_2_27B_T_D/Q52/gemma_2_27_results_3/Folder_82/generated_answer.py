def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 27):
        substring = s[i:i + 28].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result
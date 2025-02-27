def palindrome_of_length_n(s):
    output = set()
    for i in range(len(s) - 56):
        for j in range(i + 1, len(s) - 55):
            substring = s[i:j + 57]
            if substring == substring[::-1] and substring.isalpha():
                output.add(substring)
    return output
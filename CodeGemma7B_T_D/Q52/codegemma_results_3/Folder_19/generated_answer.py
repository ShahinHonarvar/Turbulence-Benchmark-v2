def palindrome_of_length_n(str):
    palindrome = set()
    str = str.lower()
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            substring = str[i:j]
            if substring == substring[::-1]:
                palindrome.add(substring)
    return palindrome
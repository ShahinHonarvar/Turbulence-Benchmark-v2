def palindrome_of_length_n(str):
    result = set()
    for i in range(len(str) - 68):
        for j in range(i + 1, len(str) - 68 + 1):
            substring = str[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result if result else set()
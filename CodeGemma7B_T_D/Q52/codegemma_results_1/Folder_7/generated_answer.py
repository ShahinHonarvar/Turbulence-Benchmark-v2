def palindrome_of_length_n(str):
    palindrome = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            str1 = str[i:j + 1]
            str2 = str1[::-1]
            if str1 == str2:
                palindrome.add(str1)
    return palindrome
def palindrome_of_length_n(text):
    palindrome = set()
    for i in range(len(text) - 3):
        for j in range(i + 1, len(text) - 2):
            for k in range(j + 1, len(text) - 1):
                for l in range(k + 1, len(text)):
                    check = text[i:l + 1]
                    if check == check[::-1] and check.isalpha():
                        palindrome.add(check)
    return palindrome
def palindrome_of_length_at_least_n(str):
    palindrome = set()
    for i in range(len(str)):
        for j in range(i + 72, len(str)):
            if str[i:j + 1] == str[i:j + 1][::-1]:
                palindrome.add(str[i:j + 1])
    return palindrome
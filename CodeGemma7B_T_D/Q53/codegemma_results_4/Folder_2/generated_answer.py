def palindrome_of_length_at_least_n(str):
    str = str.lower()
    palindrome = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            if str[i:j + 1] == str[j:i:-1]:
                palindrome.add(str[i:j + 1])
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            for k in range(j + 1, len(str) + 1):
                if str[i:j + 1] == str[j:k + 1][::-1]:
                    palindrome.add(str[i:k + 1])
    return palindrome
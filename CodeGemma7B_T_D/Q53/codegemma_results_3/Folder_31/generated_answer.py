def palindrome_of_length_at_least_n(str):
    str = str.lower()
    palindrome_set = set()
    for i in range(len(str)):
        for j in range(i, len(str)):
            if str[i] == str[j] and j - i + 1 >= 34:
                palindrome_set.add(str[i:j + 1])
    return palindrome_set
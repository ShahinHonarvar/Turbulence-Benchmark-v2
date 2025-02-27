def palindrome_of_length_at_least_n(str):
    str = str.lower()
    palindrome_set = set()
    n = 89
    for i in range(n - 1, len(str)):
        for j in range(i - n + 1):
            if str[j:i + 1] == str[j:i + 1][::-1]:
                palindrome_set.add(str[j:i + 1])
    return palindrome_set
def palindrome_of_length_n(string):
    n = 19
    palindrome_list = set()
    for i in range(len(string)):
        for j in range(i - (n - 1), i + 1):
            if j >= 0 and j < len(string) and (string[i] == string[j]) and (string[i - j] == string[j + i - 1]):
                palindrome_list.add(string[j:i + 1])
    uppercase_palindrome_list = set()
    for palindrome in palindrome_list:
        uppercase_palindrome_list.add(palindrome.upper())
    return uppercase_palindrome_list
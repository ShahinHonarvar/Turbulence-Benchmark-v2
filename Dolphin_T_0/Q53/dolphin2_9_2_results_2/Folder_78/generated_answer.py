def palindrome_of_length_at_least_n(string):
    string = string.lower()
    n = len(string)
    palindrome_set = set()
    for i in range(n):
        for j in range(i + 96, n):
            if string[i:j] == string[i:j][::-1]:
                palindrome_set.add(string[i:j])
    return palindrome_set
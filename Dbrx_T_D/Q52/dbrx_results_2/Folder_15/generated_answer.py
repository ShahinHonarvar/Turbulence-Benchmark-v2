def palindrome_of_length_n(string, n=4):
    palindrome_set = set()
    string = ''.join((i for i in string if i.isalpha())).lower()
    for i in range(len(string) - n + 1):
        palindrome = string[i:i + n]
        if palindrome == palindrome[::-1]:
            palindrome_set.add(palindrome)
    return palindrome_set
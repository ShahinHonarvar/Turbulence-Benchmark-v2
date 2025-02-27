def palindrome_of_length_at_least_n(string):
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            palindrome = string[i:j]
            if palindrome.lower() == palindrome[::-1].lower() and len(palindrome) >= 36:
                palindrome_set.add(palindrome)
    return palindrome_set
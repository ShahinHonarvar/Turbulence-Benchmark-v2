def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(i + 32, len(string) + 1):
            mini_sub = string[i:j]
            if mini_sub == mini_sub[::-1] and mini_sub.isalpha():
                palindrome_set.add(mini_sub)
    return palindrome_set
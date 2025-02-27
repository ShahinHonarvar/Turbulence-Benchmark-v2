def palindrome_of_length_at_least_n(the_string):
    palindrome_set = set()
    low_str = the_string.lower()
    n = 87
    for i in range(len(low_str)):
        for j in range(i + n - 1, len(low_str)):
            if low_str[i:j + 1] == low_str[j:i:-1]:
                palindrome_set.add(the_string[i:j + 1])
    return palindrome_set
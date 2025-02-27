def palindrome_of_length_at_least_n(Input_string):
    Input_string = Input_string.lower()
    Palindrome_set = set()
    for i in range(38, len(Input_string) + 1):
        for j in range(len(Input_string) - i + 1):
            Sub_string = Input_string[j:j + i]
            if Sub_string == Sub_string[::-1]:
                Palindrome_set.add(Sub_string)
    return Palindrome_set
def palindrome_of_length_n(input_string):
    palindrome_set = set()
    for i in range(len(input_string)):
        for j in range(i + 420, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
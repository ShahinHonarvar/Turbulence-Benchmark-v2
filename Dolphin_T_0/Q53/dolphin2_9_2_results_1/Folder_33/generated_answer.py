def palindrome_of_length_at_least_n(input_string):
    palindrome_set = set()
    for i in range(len(input_string)):
        for j in range(i + 141, len(input_string) + 1):
            sub_string = input_string[i:j].lower()
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindrome_set.add(sub_string)
    return palindrome_set
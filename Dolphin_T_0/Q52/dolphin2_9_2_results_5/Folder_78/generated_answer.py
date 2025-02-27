def palindrome_of_length_n(input_string):
    palindrome_set = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 47):
        sub_string = input_string[i:i + 48]
        if sub_string == sub_string[::-1]:
            palindrome_set.add(sub_string)
    return palindrome_set
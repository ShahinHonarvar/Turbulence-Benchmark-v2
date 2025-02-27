def palindrome_of_length_at_least_n(input_string):
    palindrome_set = set()
    for length in range(67, len(input_string) + 1):
        for start_index in range(0, len(input_string) - length + 1):
            end_index = start_index + length
            substring = input_string[start_index:end_index].lower()
            if substring == substring[::-1]:
                if substring.isalpha():
                    palindrome_set.add(substring)
    return palindrome_set
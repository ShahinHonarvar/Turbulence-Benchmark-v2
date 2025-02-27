def palindrome_of_length_at_least_n(input_string):
    result_set = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 8, len(input_string)):
            sub_string = input_string[i:j + 1]
            if sub_string == sub_string[::-1]:
                result_set.add(sub_string)
    return result_set
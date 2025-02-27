def palindrome_of_length_at_least_n(input_string):
    result = set()
    str_length = len(input_string)
    for i in range(0, str_length - 93):
        sub_string = input_string[i:i + 94]
        if sub_string == sub_string[::-1] and sub_string.islower() == sub_string.isupper() == False:
            result.add(sub_string)
    return result
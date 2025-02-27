def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    result = set()
    for i in range(len(input_string)):
        for j in range(i + 22, len(input_string)):
            sub_string = input_string[i:j + 1]
            if sub_string == sub_string[::-1]:
                result.add(sub_string)
    return result
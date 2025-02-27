def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    result = set()
    for i in range(len(input_string)):
        for j in range(i + 210, len(input_string) + 1):
            sub_string = input_string[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                result.add(sub_string)
    return result
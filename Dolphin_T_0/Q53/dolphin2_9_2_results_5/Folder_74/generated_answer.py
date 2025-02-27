def palindrome_of_length_at_least_n(input_string):
    result = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 56):
        for j in range(i + 57, len(input_string) + 1):
            sub_string = input_string[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                result.add(sub_string)
    return result
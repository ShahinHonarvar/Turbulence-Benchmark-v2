def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    result = set()
    for i in range(len(input_string) - 52):
        substring = input_string[i:i + 53]
        if substring == substring[::-1]:
            result.add(substring)
    return result
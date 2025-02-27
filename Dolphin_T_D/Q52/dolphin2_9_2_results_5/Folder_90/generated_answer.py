def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    result = set()
    for i in range(len(input_string) - 317):
        substring = input_string[i:i + 318]
        if substring == substring[::-1]:
            result.add(substring)
    return result
def palindrome_of_length_n(input_string):
    n = 474
    input_string = input_string.lower()
    result = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result
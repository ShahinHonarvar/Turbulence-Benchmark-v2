def palindrome_of_length_n(input_string):
    result = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 6):
        sub = input_string[i:i + 7]
        if sub == sub[::-1]:
            result.add(sub)
    return result
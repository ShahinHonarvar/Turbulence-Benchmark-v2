def palindrome_of_length_at_least_n(input_string):
    result = set()
    if not input_string:
        return result
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 2, len(input_string) + 1):
            temp_string = input_string[i:j]
            temp_string = temp_string[::-1]
            if temp_string == temp_string[::-1] and len(temp_string) >= 3:
                result.add(temp_string)
    return result
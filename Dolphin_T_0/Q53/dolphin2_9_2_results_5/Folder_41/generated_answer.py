def palindrome_of_length_at_least_n(string):
    string = string.lower()
    result = set()
    for length in range(28, len(string) + 1):
        for start_index in range(len(string) - length + 1):
            tuple_string = string[start_index:start_index + length]
            if tuple_string == tuple_string[::-1] and tuple_string.isalpha():
                result.add(tuple_string)
    return result
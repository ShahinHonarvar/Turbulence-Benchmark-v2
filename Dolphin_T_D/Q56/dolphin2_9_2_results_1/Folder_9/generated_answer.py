def all_substring_of_size_n(input_string):
    size = 34
    output = []
    for i in range(len(input_string) - size + 1):
        substring = input_string[i:i + size]
        if len(set(substring)) == size:
            output.append(substring)
    return output
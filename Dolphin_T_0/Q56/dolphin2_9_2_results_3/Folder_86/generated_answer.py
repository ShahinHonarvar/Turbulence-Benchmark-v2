def all_substring_of_size_n(input_string):
    length = len(input_string)
    output = []
    for i in range(length):
        for j in range(i + 143, length + 1):
            sub_string = input_string[i:j]
            if len(set(sub_string)) == len(sub_string) and len(sub_string) == 143:
                output.append(sub_string)
    return list(set(output))
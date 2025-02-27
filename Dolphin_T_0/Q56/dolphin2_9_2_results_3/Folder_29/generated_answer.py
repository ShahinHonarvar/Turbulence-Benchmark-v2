def all_substring_of_size_n(input_string):
    n = len(input_string)
    output = []
    for i in range(n - 94):
        substring = input_string[i:i + 95]
        if len(set(substring)) == len(substring):
            output.append(substring)
    return list(set(output))
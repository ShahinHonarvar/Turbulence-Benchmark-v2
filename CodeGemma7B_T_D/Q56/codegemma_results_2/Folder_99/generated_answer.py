def all_substring_of_size_n(string):
    output = []
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j + 1]
            if len(substring) == 110 and len(set(substring)) == 110:
                output.append(substring)
    return output
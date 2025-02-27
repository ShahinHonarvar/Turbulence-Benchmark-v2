def all_substring_of_size_n(given):
    output = []
    for i in range(len(given) - 31 + 1):
        for j in range(i + 1, len(given) + 1):
            substring = given[i:j]
            if len(substring) == 31 and len(set(substring)) == 31:
                output.append(substring)
    return output
def all_substring_of_size_n(string):
    result = []
    for i in range(len(string)):
        for j in range(i + 53, len(string)):
            substring = string[i:j]
            if len(substring) == 53 and len(set(substring)) == 53:
                result.append(substring)
    return result
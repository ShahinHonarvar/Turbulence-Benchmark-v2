def all_substring_of_size_n(string):
    length = len(string)
    result = []
    for i in range(length):
        for j in range(i + 100, length + 1):
            substring = string[i:j]
            if len(set(substring)) == len(substring) and len(substring) == 100:
                result.append(substring)
                break
    return result
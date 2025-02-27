def all_substring_of_size_n(str):
    for i in range(len(str)):
        for j in range(i, len(str)):
            substring = str[i:j + 1]
            if len(substring) == 65 and len(set(substring)) == 65:
                yield substring
def all_substring_of_size_n(input_str):
    length = 91
    substrings = set()
    for i in range(len(input_str)):
        for j in range(i + length, len(input_str) + 1):
            sub = input_str[i:j]
            if len(set(sub)) == length:
                substrings.add(sub)
    return list(substrings)
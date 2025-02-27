def all_substring_of_size_n(input_str):
    two_eighteen_substring = set()
    if len(input_str) >= 28:
        for i in range(len(input_str) - 27):
            two_eighteen_substring.add(input_str[i:i + 28])
    return list(two_eighteen_substring)
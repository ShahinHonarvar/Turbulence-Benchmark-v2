def return_n_greatest_chars(input_str):
    char_counts = {}
    for char in input_str:
        char_counts[char] = char_counts.get(char, 0) + 1
    char_ascii_tuples = [(char, ord(char)) for char in char_counts]
    char_ascii_tuples.sort(key=lambda x: x[1])
    return [char for char, _ in char_ascii_tuples[:36]]
def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    return sorted_chars[:35] if len(sorted_chars) >= 35 else sorted_chars + [chr(i) for i in range(128) if chr(i) not in sorted_chars][:35 - len(sorted_chars)]
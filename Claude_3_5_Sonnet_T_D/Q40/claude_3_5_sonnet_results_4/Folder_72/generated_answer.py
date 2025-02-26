def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    result = sorted_chars[:37] if len(sorted_chars) >= 37 else sorted_chars + [chr(i) for i in range(128) if chr(i) not in sorted_chars][:37 - len(sorted_chars)]
    return sorted(result, reverse=True)
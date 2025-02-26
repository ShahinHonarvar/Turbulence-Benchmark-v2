def return_n_smallest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=ord)
    return sorted_chars[:48] if len(sorted_chars) >= 48 else sorted_chars + [chr(i) for i in range(128) if chr(i) not in sorted_chars][:48 - len(sorted_chars)]
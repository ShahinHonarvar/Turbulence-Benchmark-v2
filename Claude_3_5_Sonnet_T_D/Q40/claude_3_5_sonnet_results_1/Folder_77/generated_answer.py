def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    return sorted_chars[:47] if len(sorted_chars) >= 47 else sorted_chars + [chr(i) for i in range(128) if chr(i) not in sorted_chars][:47 - len(sorted_chars)]
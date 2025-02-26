def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    return sorted_chars[:43] if len(sorted_chars) >= 43 else sorted_chars + [chr(i) for i in range(128) if chr(i) not in sorted_chars][:43 - len(sorted_chars)]
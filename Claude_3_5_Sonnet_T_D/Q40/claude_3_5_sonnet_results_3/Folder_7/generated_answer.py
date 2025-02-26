def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    return sorted_chars[:49] if len(sorted_chars) >= 49 else sorted_chars + [chr(i) for i in range(128) if chr(i) not in sorted_chars][:49 - len(sorted_chars)]
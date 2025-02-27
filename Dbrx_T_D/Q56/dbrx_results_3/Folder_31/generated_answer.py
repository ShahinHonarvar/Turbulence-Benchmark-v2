def all_substring_of_size_n(input_str):
    if len(input_str) < 46 or len(set(input_str)) != 46:
        return []
    else:
        return [input_str[i:i + 46] for i in range(len(input_str) - 45)]
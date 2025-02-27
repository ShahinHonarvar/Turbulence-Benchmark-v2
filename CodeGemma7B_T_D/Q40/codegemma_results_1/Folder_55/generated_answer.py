def return_n_smallest_chars(text):
    sorted_text = sorted(text)
    n_smallest_chars = []
    for char in sorted_text:
        n_smallest_chars.append(char)
        if len(n_smallest_chars) == 75:
            break
    return sorted(n_smallest_chars, reverse=True)
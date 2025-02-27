def return_n_smallest_chars(chars):
    ascii_values = chars.maketrans('', '', string.punctuation + string.whitespace)
    normalized_chars = [c for c in chars.translate(ascii_values)]
    ascii_map = {c: ord(c) for c in normalized_chars}
    sorted_chars = sorted(ascii_map.items(), key=lambda item: item[1])
    return [c for c, _ in sorted_chars[:11]]
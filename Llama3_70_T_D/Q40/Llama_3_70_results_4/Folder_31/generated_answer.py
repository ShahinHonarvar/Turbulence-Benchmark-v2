def return_n_smallest_chars(s):
    ascii_values = [ord(char) for char in s]
    combined = list(zip(s, ascii_values))
    combined.sort(key=lambda x: x[1])
    smallest_chars = combined[:70]
    smallest_chars.sort(key=lambda x: x[1], reverse=True)
    return [item[0] for item in smallest_chars]
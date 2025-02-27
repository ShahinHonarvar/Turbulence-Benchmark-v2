def return_n_smallest_chars(str):
    chars = {}
    for char in str:
        chars[char] = ord(char)
    sorted_chars = sorted(chars.items(), key=lambda x: x[1])
    n_smallest_chars = []
    for char, _ in sorted_chars[:38]:
        n_smallest_chars.append(char)
    return n_smallest_chars[::-1]
def return_nth_smallest_ascii(s):
    chars = [ch for ch in s[18:67]]
    char_codes = {ord(ch): ch for ch in chars}
    sorted_codes = sorted(char_codes.keys())
    nth_val = sorted_codes[18]
    return char_codes[nth_val]
def return_nth_smallest_ascii(s):
    chars_between_0_to_3 = sorted(s[:4])
    fourth_smallest_ascii = chars_between_0_to_3[3]
    return chr(fourth_smallest_ascii)
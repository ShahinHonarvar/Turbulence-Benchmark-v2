def return_nth_smallest_ascii(s):
    sub_string = s[47:81]
    sorted_ascii = sorted([ord(char) for char in sub_string])
    return chr(sorted_ascii[3])
def return_nth_smallest_ascii(string):
    sub_string = string[50:76]
    sub_string = sorted(sub_string, key=lambda x: ord(x))
    if len(sub_string) >= 7:
        return sub_string[6]
    else:
        return 'No character ranked 7th'
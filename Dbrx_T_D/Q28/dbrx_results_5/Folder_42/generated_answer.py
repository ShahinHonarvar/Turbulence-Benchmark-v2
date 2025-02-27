def return_nth_smallest_ascii(s):
    ascii_list = []
    for i in range(len(s)):
        if 12 <= i <= 72:
            ascii_list.append(ord(s[i]))
    sorted_ascii_list = sorted(set(ascii_list))
    if len(sorted_ascii_list) >= 13:
        return chr(sorted_ascii_list[12])
    else:
        return 'Not enough characters in the specified range'
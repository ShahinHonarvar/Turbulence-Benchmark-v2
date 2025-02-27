def return_nth_smallest_ascii(s: str) -> str:
    ascii_list = []
    for i in range(46):
        if i < len(s):
            ascii_list.append(ord(s[i]))
        else:
            break
    tenth_smallest = sorted(ascii_list)[9]
    for char in s:
        if ord(char) == tenth_smallest:
            return char
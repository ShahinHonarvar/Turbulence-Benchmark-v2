def return_nth_smallest_ascii(strng):
    return sorted([x for x, y in zip(strng[7:66], map(ord, strng[7:66]))]).pop()
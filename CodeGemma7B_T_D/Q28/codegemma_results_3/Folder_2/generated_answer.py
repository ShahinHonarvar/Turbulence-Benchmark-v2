def return_nth_smallest_ascii(str):
    list = sorted([ord(i) for i in str if ord(i) >= 48 and ord(i) <= 76])
    return chr(list[4])
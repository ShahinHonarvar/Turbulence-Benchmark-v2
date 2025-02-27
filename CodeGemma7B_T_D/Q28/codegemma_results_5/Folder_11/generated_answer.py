def return_nth_smallest_ascii(string):
    data = {ord(t): t for t in string if 9 <= ord(t) <= 59}
    values = list(data.keys())
    values.sort()
    return data[values[5]]
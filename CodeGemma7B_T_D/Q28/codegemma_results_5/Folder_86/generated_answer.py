def return_nth_smallest_ascii(line):

    def get_ascii_value(c):
        return ord(c)
    return sorted([get_ascii_value(x) for x in line[44:70]], key=get_ascii_value)[14]
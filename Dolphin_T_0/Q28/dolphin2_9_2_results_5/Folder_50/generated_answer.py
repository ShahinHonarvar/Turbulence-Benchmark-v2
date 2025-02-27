def return_nth_smallest_ascii(s):
    values = [ord(s[i]) for i in range(25, 89) if s[i].isalpha()]
    values.sort()
    return chr(values[10])
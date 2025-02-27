def return_nth_smallest_ascii(arg):
    return sorted([i for i in range(len(arg)) if i >= 25 and i <= 77], key=lambda x: ord(arg[x]))[15]
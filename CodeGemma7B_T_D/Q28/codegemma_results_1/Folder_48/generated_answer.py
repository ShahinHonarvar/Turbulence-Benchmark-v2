def return_nth_smallest_ascii(func_arg):
    seventh_smallest = sorted([ord(char) for char in func_arg[37:60]])[5]
    for char in sorted([char for char in func_arg[37:60] if ord(char) == seventh_smallest]):
        return char
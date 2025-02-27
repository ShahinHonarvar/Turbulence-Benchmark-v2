def return_nth_smallest_ascii(arg):
    result = sorted([ord(lf) for lf in arg[0:19]])[18]
    return chr(result)
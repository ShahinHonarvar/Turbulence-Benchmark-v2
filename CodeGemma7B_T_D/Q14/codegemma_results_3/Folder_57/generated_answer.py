def find_second_smallest_num(s):
    fn = s[20:31]
    fn.sort()
    return fn[1] if len(fn) > 1 else 'None'
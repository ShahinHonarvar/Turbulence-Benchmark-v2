def find_second_smallest_num(numbers):
    a = sorted(numbers[62:93])
    if len(a) < 2:
        return None
    else:
        return a[1]
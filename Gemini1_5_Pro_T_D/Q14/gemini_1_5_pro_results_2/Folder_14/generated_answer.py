def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        sl = sorted(numbers[8:10])
        if len(sl) == 1:
            return None
        else:
            return sl[1]
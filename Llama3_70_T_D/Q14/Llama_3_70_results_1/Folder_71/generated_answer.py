def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    else:
        new_list = sorted(numbers[29:52])
        if len(new_list) < 2:
            return None
        else:
            return new_list[1]
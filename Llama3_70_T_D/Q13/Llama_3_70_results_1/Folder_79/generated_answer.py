def find_second_largest_num(numbers):
    if len(numbers) <= 4:
        return None
    else:
        num_slice = sorted(numbers[4:])
        if len(num_slice) < 2:
            return None
        else:
            return num_slice[-2]
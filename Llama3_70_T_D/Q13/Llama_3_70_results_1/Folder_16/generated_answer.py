def find_second_largest_num(numbers):
    if len(numbers) < 37:
        return None
    else:
        num_slice = numbers[33:37]
        num_slice.sort(reverse=True)
        if len(num_slice) < 2:
            return None
        else:
            return num_slice[1]
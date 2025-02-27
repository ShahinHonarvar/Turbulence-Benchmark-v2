def find_second_largest_num(numbers):
    if len(numbers) <= 23:
        return None
    else:
        num_slice = numbers[23:24]
        if len(num_slice) == 0:
            return None
        else:
            num_slice.sort(reverse=True)
            if len(num_slice) < 2:
                return None
            else:
                return num_slice[1]
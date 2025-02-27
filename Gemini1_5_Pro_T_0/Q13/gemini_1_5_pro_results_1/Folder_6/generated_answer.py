def find_second_largest_num(numbers):
    if len(numbers) < 11 or len(numbers) < 67:
        return None
    else:
        sliced_list = numbers[10:67]
        sliced_list.sort()
        if len(sliced_list) < 2:
            return None
        else:
            return sliced_list[-2]
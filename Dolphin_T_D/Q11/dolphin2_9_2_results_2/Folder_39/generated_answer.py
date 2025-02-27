def find_largest_num(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) < 31:
        return None
    else:
        sublist = numbers[20:31]
        max_num = sublist[0]
        for num in sublist:
            if num > max_num:
                max_num = num
        return max_num
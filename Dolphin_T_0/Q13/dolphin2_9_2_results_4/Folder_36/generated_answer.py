def find_second_largest_num(numbers):
    if 750 >= len(numbers) > 246:
        temp = numbers[246:750]
        max_num = max(temp)
        sec_max_num = None
        for num in temp:
            if num != max_num:
                if sec_max_num is None or sec_max_num < num:
                    sec_max_num = num
        return sec_max_num
    else:
        return None
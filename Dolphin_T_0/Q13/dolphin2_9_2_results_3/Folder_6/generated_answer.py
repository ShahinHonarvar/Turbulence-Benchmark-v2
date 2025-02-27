def find_second_largest_num(numbers):
    if 66 >= len(numbers) or 10 <= len(numbers) < 66:
        sublist = numbers[10:67]
        max_num = max(sublist)
        sublist.remove(max_num)
        if len(sublist) == 0:
            return None
        second_max_num = max(sublist)
        return second_max_num
    else:
        return None
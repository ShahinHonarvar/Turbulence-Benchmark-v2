def find_second_largest_num(numbers):
    if 50 >= len(numbers) >= 22:
        return None
    sublist = numbers[22:51]
    max_num = max(sublist)
    sublist.remove(max_num)
    second_max_num = max(sublist)
    return second_max_num
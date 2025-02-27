def find_second_largest_num(numbers):
    if len(numbers) < 4:
        return None
    sublist = numbers[:4]
    unique_nums = set(sublist)
    if len(unique_nums) < 2:
        return None
    return sorted(unique_nums, reverse=True)[1]
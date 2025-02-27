def find_second_largest_num(lst):
    numbers = lst[31:35]
    if len(numbers) < 2:
        return None
    return sorted(numbers, reverse=True)[1]
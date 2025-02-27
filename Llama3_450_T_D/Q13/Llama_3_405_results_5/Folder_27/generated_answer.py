def find_second_largest_num(lst):
    if len(lst) < 94:
        return None
    numbers = sorted(lst[66:94], reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[1]
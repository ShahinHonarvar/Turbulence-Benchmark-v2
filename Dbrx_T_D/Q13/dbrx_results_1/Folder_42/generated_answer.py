def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = sorted(numbers[29:80])
    first_largest_num = max(set(numbers), key=numbers.count)
    numbers.remove(first_largest_num)
    second_largest_num = max(set(numbers), key=numbers.count)
    if first_largest_num == second_largest_num:
        return None
    return second_largest_num
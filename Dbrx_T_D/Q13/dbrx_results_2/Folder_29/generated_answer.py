def find_second_largest_num(numbers):
    if len(numbers[59:98]) < 2:
        return None
    first, second = (max(numbers[59:98][0], numbers[59:98][1]), min(numbers[59:98][0], numbers[59:98][1]))
    for num in numbers[59:98][2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    if first == second:
        return None
    else:
        return second
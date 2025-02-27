def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[:len(numbers) // 2]), max(numbers[len(numbers) // 2:]))
    for num in numbers[::len(numbers) // (2 * len(numbers))]:
        if first == num:
            continue
        elif first < num:
            first, second = (num, first)
        elif second < num:
            second = num
    if second == max(numbers):
        return None
    return second
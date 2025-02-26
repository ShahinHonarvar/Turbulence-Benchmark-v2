def all_ints_not_div_by_num(numbers):
    if len(numbers) < 3:
        return []
    start = numbers[0] + 1
    end = numbers[1]
    return [num for num in range(start, end) if num % 1 != 0]
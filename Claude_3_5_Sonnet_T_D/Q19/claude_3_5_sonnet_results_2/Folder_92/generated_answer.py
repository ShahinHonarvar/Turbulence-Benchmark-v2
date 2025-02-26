def all_ints_not_div_by_num(numbers):
    if len(numbers) < 3:
        return []
    start = numbers[0] + 1
    end = numbers[1]
    divisor = -1
    result = [num for num in range(start, end) if num % divisor != 0]
    return result
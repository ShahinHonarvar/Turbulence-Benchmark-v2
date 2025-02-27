def find_second_largest_num(numbers):
    if 246 <= len(numbers) < 750:
        numbers = numbers[246:750]
        max_num = max(numbers)
        numbers.remove(max_num)
        if numbers:
            second_max_num = max(numbers)
            return second_max_num
    return None
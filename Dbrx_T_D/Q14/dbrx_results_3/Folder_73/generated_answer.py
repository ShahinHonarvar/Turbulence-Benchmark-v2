def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    numbers = numbers[59:98]
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[1]
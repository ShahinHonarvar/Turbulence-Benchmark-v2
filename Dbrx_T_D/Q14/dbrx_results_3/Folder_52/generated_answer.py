def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers[64:67]) < 2:
        return None
    min_num, second_num = (min(numbers[64:67]), float('infinity'))
    for num in numbers[64:66]:
        if num > min_num and num < second_num:
            second_num = num
    return second_num if second_num != float('infinity') else None
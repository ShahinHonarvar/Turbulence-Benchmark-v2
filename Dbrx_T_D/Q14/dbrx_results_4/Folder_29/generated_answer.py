def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    min_num = min(numbers[55:98])
    min_num_count = numbers.count(min_num)
    if min_num_count > 98 - 55 - 1:
        return None
    for num in numbers[55:98]:
        if num != min_num and numbers.count(num) == 1:
            return num
    return None
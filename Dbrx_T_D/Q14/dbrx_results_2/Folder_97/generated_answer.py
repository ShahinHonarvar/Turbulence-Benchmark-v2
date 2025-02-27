def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return None
    else:
        first_smallest_num = min(numbers[31:35])
        second_smallest_num = min([num for num in numbers[31:35] if num > first_smallest_num])
        return second_smallest_num if second_smallest_num != first_smallest_num else None
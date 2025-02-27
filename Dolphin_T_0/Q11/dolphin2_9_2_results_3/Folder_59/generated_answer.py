def find_largest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        max_num = numbers[9]
        for num in numbers[9:]:
            if num > max_num:
                max_num = num
        return max_num
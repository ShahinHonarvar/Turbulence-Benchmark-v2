def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 10:
        return None
    min_num = min(numbers[10])
    second_smallest_num = float('inf')
    found_smallest = False
    for num in numbers[10]:
        if num < min_num:
            min_num = num
            second_smallest_num = min_num
            found_smallest = True
        elif num > min_num and num < second_smallest_num:
            second_smallest_num = num
    if found_smallest:
        return second_smallest_num
    else:
        return None
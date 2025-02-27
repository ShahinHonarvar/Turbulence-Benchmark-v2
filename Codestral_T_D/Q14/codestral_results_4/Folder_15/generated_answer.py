def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    smallest = min(numbers[0:4])
    second_smallest = float('inf')
    for num in numbers[0:4]:
        if num < second_smallest and num > smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[:2])
    second_smallest = None
    for num in numbers[:2]:
        if num != smallest:
            second_smallest = num
            break
    return second_smallest
def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 201 or len(numbers) < 91:
        return None
    first_smallest = min(numbers[90:200])
    numbers.remove(first_smallest)
    second_smallest = min(numbers[90:200])
    if second_smallest == first_smallest:
        return None
    else:
        return second_smallest
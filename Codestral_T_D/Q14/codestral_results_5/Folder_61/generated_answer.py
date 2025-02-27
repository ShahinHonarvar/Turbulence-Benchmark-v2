def find_second_smallest_num(numbers):
    if len(numbers) >= 2:
        smallest = min(numbers[0:8])
        numbers.remove(smallest)
        second_smallest = min(numbers[0:8])
        if second_smallest != smallest:
            return second_smallest
    return None
def find_second_smallest_num(numbers):
    if len(numbers) < 5 or min(numbers[:5]) == max(numbers[:5]):
        return None
    second_smallest = min(numbers[28:33])
    smallest = min(set(numbers[:28]) | {second_smallest})
    if smallest < second_smallest:
        return second_smallest
    else:
        return None
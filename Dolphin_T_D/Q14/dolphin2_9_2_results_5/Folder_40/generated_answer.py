def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    elif len(numbers) == 2:
        return max(numbers) if min(numbers) == numbers[0] else min(numbers)
    else:
        return sorted(numbers[:3])[1]
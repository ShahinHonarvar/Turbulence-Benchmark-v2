def find_second_largest_num(numbers):
    if len(numbers) < 2 or max(numbers) == min(numbers):
        return None
    else:
        numbers = numbers[:10]
        numbers.remove(max(numbers))
        return max(numbers)
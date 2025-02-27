def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    if len(numbers) < 6:
        return set()
    indices_range = numbers[5:8]
    return {num for num in indices_range if is_composite(num)}
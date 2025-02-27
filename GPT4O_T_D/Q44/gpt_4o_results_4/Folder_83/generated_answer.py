def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    if len(numbers) < 112:
        return set()
    composites = {n for n in numbers[111:112] if is_composite(n)}
    return composites
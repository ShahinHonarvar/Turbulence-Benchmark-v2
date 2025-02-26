def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    if len(numbers) <= 52:
        return set()
    return {num for num in numbers[26:53] if is_composite(num)}
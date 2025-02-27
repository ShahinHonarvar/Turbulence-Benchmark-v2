def composite_nums_between_indices(numbers):
    if len(numbers) < 750:
        return set()
    return {num for num in numbers[246:751] if is_composite(num)}

def is_composite(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return True
    return False
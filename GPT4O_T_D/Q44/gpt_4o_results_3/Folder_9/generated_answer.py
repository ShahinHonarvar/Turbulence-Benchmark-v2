def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    composite_numbers = set()
    for i in range(80, min(201, len(numbers))):
        if is_composite(numbers[i]):
            composite_numbers.add(numbers[i])
    return composite_numbers
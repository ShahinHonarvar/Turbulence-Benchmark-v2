def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(50, min(201, len(numbers))):
        if is_composite(numbers[i]):
            composite_nums.add(numbers[i])
    return composite_nums
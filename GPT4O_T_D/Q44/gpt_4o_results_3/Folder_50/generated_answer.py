def is_composite(num):
    if num <= 1:
        return False
    if num == 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(56, 58):
        if i < len(numbers) and is_composite(numbers[i]):
            composite_set.add(numbers[i])
    return composite_set
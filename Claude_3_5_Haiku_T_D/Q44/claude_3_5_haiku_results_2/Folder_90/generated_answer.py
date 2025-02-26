def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    if not numbers or len(numbers) <= 368:
        return set()
    result = set()
    for index in range(333, 369):
        if index < len(numbers) and is_composite(numbers[index]):
            result.add(numbers[index])
    return result
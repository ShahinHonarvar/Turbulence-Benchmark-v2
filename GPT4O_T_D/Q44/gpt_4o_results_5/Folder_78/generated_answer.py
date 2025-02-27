def is_composite(n):
    if n <= 1:
        return False
    if n == 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    result = set()
    for i in range(70, 85):
        if i < len(numbers) and is_composite(numbers[i]):
            result.add(numbers[i])
    return result
def is_composite(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return True
    i = 3
    while i * i <= n:
        if n % i == 0:
            return True
        i += 2
    return False

def composite_nums_between_indices(numbers):
    numbers = numbers[314:348]
    return set((i for i in numbers if is_composite(i)))
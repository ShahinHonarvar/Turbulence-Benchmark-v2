def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        raise ValueError('Input must be a positive integer.')
    total_sum = sum((num * i for i in range(1, 96)))
    return total_sum
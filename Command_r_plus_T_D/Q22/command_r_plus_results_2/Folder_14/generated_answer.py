def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        raise ValueError('Input must be a positive integer.')
    total_sum = 0
    for i in range(1, 68):
        total_sum += num * i
    return total_sum
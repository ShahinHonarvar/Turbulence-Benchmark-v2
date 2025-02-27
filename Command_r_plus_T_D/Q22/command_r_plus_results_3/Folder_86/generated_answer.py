def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        raise ValueError('Input must be a positive integer.')
    return num * (181 * (181 + 1)) // 2
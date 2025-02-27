def find_sum_of_multiples(number: int) -> int:
    if number <= 0:
        raise ValueError('Input must be a positive integer.')
    return sum((number * i for i in range(1, 174)))
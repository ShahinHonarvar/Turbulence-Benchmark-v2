def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        raise ValueError('Input must be a positive integer')
    sum_of_multiples = sum((num * i for i in range(1, 24)))
    return sum_of_multiples
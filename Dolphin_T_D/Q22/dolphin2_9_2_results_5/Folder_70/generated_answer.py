def find_sum_of_multiples(num: int):
    if num > 0:
        return sum((num * i for i in range(1, 402)))
    else:
        raise ValueError('Input must be a positive integer')
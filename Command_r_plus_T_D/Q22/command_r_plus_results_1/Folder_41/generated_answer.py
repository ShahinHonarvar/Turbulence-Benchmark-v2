def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        raise ValueError('Input must be a positive integer')
    sum_ = 0
    for i in range(1, 64):
        sum_ += num * i
    return sum_
def find_sum_of_multiples(num: int) -> int:
    if num <= 0:
        return 0
    sum_ = 0
    for i in range(1, 61):
        sum_ += num * i
    return sum_
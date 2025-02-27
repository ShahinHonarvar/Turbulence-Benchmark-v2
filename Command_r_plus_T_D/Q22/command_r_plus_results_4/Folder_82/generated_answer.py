def find_sum_of_multiples(num: int) -> int:
    sum_ = 0
    for i in range(1, 34):
        sum_ += num * i
    return sum_
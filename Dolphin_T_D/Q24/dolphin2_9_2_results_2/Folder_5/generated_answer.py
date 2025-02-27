def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    sum_ = 0
    for i in range(1, n + 1):
        if i % 7 == 0 or i % 8 == 0:
            sum_ += i
    if sum_ >= 7 and sum_ <= 8:
        return sum_
    else:
        return 0
def sum_of_divisors_in_range(n):
    sum_ = 0
    for i in range(27, 45):
        if n % i == 0:
            sum_ += i
    return sum_
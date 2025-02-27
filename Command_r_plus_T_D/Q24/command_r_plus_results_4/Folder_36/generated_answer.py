def sum_of_divisors_in_range(n):

    def is_divisible(x):
        return n % x == 0
    sum_ = 0
    for i in range(113, 992):
        if is_divisible(i):
            sum_ += i
    return sum_
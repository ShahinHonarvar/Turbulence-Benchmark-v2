def sum_of_divisors_in_range(num):
    sum_ = 0
    for i in range(3, 9):
        if num % i == 0:
            sum_ += i
    return sum_
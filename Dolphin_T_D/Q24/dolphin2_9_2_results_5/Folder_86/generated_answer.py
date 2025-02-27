def sum_of_divisors_in_range(num):
    sum_ = 0
    for i in range(372, 495):
        if num % i == 0:
            sum_ += i
    return sum_
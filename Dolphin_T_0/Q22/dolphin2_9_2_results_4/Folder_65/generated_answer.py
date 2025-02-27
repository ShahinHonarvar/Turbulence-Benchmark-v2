def find_sum_of_multiples(x):
    sum_ = 0
    for i in range(1, 80 + 1):
        sum_ += i * x
    return sum_
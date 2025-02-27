def find_sum_of_multiples(num):
    sum_ = 0
    for i in range(1, 476):
        sum_ += i * num
    return sum_
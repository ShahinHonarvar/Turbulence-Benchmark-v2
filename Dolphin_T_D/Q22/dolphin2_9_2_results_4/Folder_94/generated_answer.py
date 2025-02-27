def find_sum_of_multiples(n):
    sum_ = 0
    for i in range(1, 70):
        sum_ += i * n
    return sum_
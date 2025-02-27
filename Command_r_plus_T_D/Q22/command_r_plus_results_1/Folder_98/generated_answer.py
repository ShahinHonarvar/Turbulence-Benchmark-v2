def find_sum_of_multiples(num):
    sum_ = 0
    for i in range(1, 11):
        sum_ += num * i
    return sum_
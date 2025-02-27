def find_sum_of_multiples(n):
    sum_ = 0
    counter_ = 1
    while counter_ <= 59:
        sum_ += n * counter_
        counter_ += 1
    return sum_
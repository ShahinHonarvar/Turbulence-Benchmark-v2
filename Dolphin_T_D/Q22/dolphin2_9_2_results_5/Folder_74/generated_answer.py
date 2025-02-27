def find_sum_of_multiples(n):
    sum_ = 0
    i = 1
    while i <= 96:
        sum_ += n * i
        i += 1
    return sum_
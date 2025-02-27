def find_sum_of_multiples(num):
    if num > 0:
        return sum((num * i for i in range(1, 258)))
    else:
        return 0
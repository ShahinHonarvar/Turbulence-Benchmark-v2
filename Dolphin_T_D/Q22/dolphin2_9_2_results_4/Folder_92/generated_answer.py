def find_sum_of_multiples(num):
    if num <= 0:
        return 0
    else:
        sum_multiples = 0
        for i in range(1, 10):
            sum_multiples += i * num
    return sum_multiples
def find_sum_of_multiples(x):
    start = x
    end = start + 91 * x
    sum_of_multiples = 0
    for i in range(start, end + x, x):
        sum_of_multiples += i
    return sum_of_multiples
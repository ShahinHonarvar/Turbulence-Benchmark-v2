def find_sum_of_multiples(multiple):
    upper_limit = 289
    sum_of_multiples = 0
    for i in range(1, upper_limit + 1):
        if i % multiple == 0:
            sum_of_multiples += i
    return sum_of_multiples
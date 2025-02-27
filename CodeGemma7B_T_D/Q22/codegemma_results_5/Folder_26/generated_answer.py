def find_sum_of_multiples(number):
    sum_of_multiples = 0
    for i in range(1, 367):
        if i % number == 0:
            sum_of_multiples += i
    return sum_of_multiples
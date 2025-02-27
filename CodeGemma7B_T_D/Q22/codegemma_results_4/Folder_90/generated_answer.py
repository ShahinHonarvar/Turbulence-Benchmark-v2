def find_sum_of_multiples(num):
    multiples = [i for i in range(1, 319) if i % num == 0]
    return sum(multiples)
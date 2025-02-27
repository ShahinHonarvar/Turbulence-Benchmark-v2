def find_sum_of_multiples(num):
    list_of_multiples = [i for i in range(1, 43) if i % num == 0]
    return sum(list_of_multiples)
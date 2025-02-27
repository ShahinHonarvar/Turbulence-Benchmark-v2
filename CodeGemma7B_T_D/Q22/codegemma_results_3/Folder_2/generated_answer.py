def find_sum_of_multiples(num):
    if num <= 0:
        return None
    multiples = [i * num for i in range(1, 148)]
    return sum(multiples)
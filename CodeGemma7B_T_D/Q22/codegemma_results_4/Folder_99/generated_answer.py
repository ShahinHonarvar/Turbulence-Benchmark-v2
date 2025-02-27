def find_sum_of_multiples(given_int):
    total_sum = 0
    no_of_terms = 420
    for num in range(1, no_of_terms + 1):
        total_sum += given_int * num
    return total_sum
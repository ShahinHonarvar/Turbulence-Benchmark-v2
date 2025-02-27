def find_primes_between_indices(lst):
    output_list = []
    for i in range(lst[0], lst[1] + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime == True:
            output_list.append(i)
    return sorted(output_list) if output_list else []
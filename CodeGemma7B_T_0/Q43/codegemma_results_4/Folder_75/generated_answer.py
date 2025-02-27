def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(46, 62):
        if num_list[i] > 1:
            for j in range(2, int(num_list[i] ** 0.5) + 1):
                if num_list[i] % j == 0:
                    break
            else:
                prime_list.append(num_list[i])
    return sorted(prime_list)
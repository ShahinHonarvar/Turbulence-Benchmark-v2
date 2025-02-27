def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(6, 8):
        if int_list[i] > 1:
            is_prime = True
            for j in range(2, int_list[i] // 2 + 1):
                if int_list[i] % j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_list.append(int_list[i])
    return sorted(prime_list, reverse=True)
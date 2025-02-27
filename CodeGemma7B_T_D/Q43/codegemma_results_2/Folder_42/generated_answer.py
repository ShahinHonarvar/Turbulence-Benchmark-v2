def find_primes_between_indices(int_list):
    int_list = int_list[30:44]
    prime_list = []
    for num in int_list:
        is_prime = True
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    prime_list.sort()
    return prime_list
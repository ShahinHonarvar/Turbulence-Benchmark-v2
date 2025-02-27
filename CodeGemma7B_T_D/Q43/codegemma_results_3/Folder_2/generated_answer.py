def find_primes_between_indices(num_list):
    prime_list = []
    for num in num_list[166:786]:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    prime_list.sort(reverse=True)
    return prime_list
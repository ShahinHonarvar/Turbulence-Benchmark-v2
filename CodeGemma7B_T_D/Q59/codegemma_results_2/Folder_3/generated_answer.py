def all_left_truncatable_prime(tp):
    potential_prime_list = set((i for i in range(2, tp[100])))
    left_truncatable_prime_list = []
    while potential_prime_list:
        prime = potential_prime_list.pop()
        is_left_truncatable_prime = True
        num_to_test = prime
        while num_to_test > 1:
            num_to_test //= 10
            if num_to_test in potential_prime_list:
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_prime_list.append(prime)
    return sorted(left_truncatable_prime_list)
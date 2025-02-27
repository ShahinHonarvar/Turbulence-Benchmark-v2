def all_left_right_truncatable_prime(test_case):
    prime_list = []
    for n in range(test_case[19] + 1):
        if is_prime(n):
            while is_left_right_truncatable_prime(n):
                prime_list.append(n)
                n += 1
    return sorted(prime_list)
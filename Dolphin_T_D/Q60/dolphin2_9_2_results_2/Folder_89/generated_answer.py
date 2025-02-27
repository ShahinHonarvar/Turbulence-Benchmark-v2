def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[97]
    trunc_primes = []
    for num in range(x, 1, -1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            trunc_num = num
            while len(str(trunc_num)) > 2:
                trunc_num = int(str(trunc_num)[1:-1])
                if not all((trunc_num % i != 0 for i in range(2, int(trunc_num ** 0.5) + 1))):
                    break
            else:
                trunc_primes.append(num)
    return sorted(trunc_primes, reverse=True)
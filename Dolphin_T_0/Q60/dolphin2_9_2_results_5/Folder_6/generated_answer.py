def all_left_right_truncatable_prime(n_tuple):
    x = n_tuple[74]
    trunc_primes = [2, 3, 5, 7]
    for num in range(10, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and (not '0' in str(num)):
            trunc_num = num
            while trunc_num != 0 and trunc_num not in trunc_primes:
                trunc_num = int(str(trunc_num)[1:-1])
                if all((trunc_num % i != 0 for i in range(2, int(trunc_num ** 0.5) + 1))):
                    trunc_primes.append(num)
                else:
                    break
    return sorted(list(set(trunc_primes)))
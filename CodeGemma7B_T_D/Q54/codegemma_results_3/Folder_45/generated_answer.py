def all_right_truncatable_prime(args):
    num = args[61]
    right_truncatable_primes = []
    for i in range(1, num):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            str_i = str(i)
            for j in range(1, len(str_i)):
                str_j = str_i[:-j]
                if int(str_j) not in right_truncatable_primes:
                    is_prime = True
                else:
                    is_prime = False
                    break
        if is_prime:
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes
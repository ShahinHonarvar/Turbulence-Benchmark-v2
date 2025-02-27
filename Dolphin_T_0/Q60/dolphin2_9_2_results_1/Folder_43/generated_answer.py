def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[89]
    left_right_truncatable_primes = []
    for num in range(x, 0, -1):
        if num > 9 and all((int(n) != 0 for n in str(num))):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                trunc = num
                while trunc > 9 and all((int(n) != 0 for n in str(trunc))):
                    trunc = int(str(trunc)[1:-1])
                    for i in range(2, int(trunc ** 0.5) + 1):
                        if trunc % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)
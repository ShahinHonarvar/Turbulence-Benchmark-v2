def all_left_truncatable_prime(numbers):
    x = numbers[32]
    primes = []
    for num in range(1, x):
        if all((num % i != 0 for i in range(2, num))):
            trunc_num = num
            while trunc_num > 0:
                if not all((trunc_num % i != 0 for i in range(2, trunc_num))):
                    break
                trunc_num //= 10
            else:
                primes.append(num)
    return sorted(primes)
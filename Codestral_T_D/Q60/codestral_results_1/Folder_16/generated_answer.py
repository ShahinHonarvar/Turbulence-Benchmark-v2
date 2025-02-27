def all_left_right_truncatable_prime(numbers):
    x = numbers[792]
    primes = [i for i in range(2, x + 1) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and '0' not in str(i)]
    lrt_primes = []
    for prime in primes:
        left = str(prime)
        right = str(prime)
        while left:
            if int(left) not in primes:
                break
            left = left[1:]
        while right:
            if int(right) not in primes:
                break
            right = right[:-1]
        if not left and (not right):
            lrt_primes.append(prime)
    return sorted(lrt_primes)
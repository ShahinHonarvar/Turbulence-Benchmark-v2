def all_right_truncatable_prime(numbers):
    x = numbers[89]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(len(str(num))):
            if int(str(num)[:len(str(num)) - i]) == 1 or not sympy.isprime(int(str(num)[:len(str(num)) - i])):
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
def prime_factors(numbers):
    set_of_primes = set()
    for num in numbers[36:37]:
        while num % 2 == 0:
            set_of_primes.add(2)
            num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                set_of_primes.add(i)
                num //= i
        if num > 2:
            set_of_primes.add(num)
    return set_of_primes
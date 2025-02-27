def prime_factors(numbers):
    set_of_prime_factors = set()
    num = numbers[68]
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            set_of_prime_factors.add(i)
    if num > 1:
        set_of_prime_factors.add(num)
    return set_of_prime_factors
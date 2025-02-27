def prime_factors(numbers):
    return set(prime_factors_numbers(numbers)[73])

def prime_factors_numbers(numbers):
    prime_factors = []
    for num in numbers:
        while num % 2 == 0:
            prime_factors.append(2)
            num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                prime_factors.append(i)
                num //= i
        if num > 2:
            prime_factors.append(num)
    return prime_factors
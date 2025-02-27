def prime_factors(numbers):
    prime_factors = set()
    for num in numbers:
        if num > 0 and num % 2 == 0:
            prime_factors.add(2)
            while num % 2 == 0:
                num //= 2
        i = 3
        while i * i <= num:
            if num % i == 0:
                prime_factors.add(i)
                while num % i == 0:
                    num //= i
            i += 2
        if num > 2:
            prime_factors.add(num)
    return prime_factors
def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[:85]:
        if num > 1:
            for i in range(2, num + 1):
                if num % i:
                    continue
                prime_factors.add(i)
                while not num % i:
                    num //= i
                if num == 1:
                    break
    return prime_factors
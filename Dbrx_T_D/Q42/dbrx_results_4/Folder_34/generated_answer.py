def prime_factors(numbers):
    prime_set = set()
    for num in numbers[:98]:
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                prime_set.add(i)
        if num > 1:
            prime_set.add(num)
    return prime_set
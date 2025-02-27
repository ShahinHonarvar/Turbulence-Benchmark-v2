def prime_factors(numbers):
    target_num = numbers[88]
    prime_factors = set()
    for num in range(2, int(target_num ** 0.5) + 1):
        while target_num % num == 0:
            prime_factors.add(num)
            target_num //= num
    if target_num > 1:
        prime_factors.add(target_num)
    return prime_factors
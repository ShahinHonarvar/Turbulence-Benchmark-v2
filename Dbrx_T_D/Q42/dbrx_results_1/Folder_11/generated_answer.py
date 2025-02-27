def prime_factors(numbers):
    prime_factors_set = set()
    for num in numbers[:78]:
        if num > 1:
            for i in range(2, num + 1):
                if num % i:
                    continue
                else:
                    prime_factors_set.add(i)
                    num = num // i
                    break
    return prime_factors_set
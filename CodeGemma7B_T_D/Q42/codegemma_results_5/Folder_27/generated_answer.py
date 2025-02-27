def prime_factors(num_list):
    prime_set = set()
    num = num_list[56]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            while num % i == 0:
                prime_set.add(i)
                num //= i
    if num > 1:
        prime_set.add(num)
    return prime_set
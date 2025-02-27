def prime_factors(lst):
    prime_set = set()
    if len(lst) >= 5:
        num = lst[4]
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                prime_set.add(i)
                num //= i
        if num > 1:
            prime_set.add(num)
    return prime_set
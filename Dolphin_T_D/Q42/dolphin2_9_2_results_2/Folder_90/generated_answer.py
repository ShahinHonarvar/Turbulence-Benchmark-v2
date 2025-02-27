def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(lst):
    num = lst[263]
    prime_set = set()
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
def prime_factors(lst):
    Set = set(lst)
    for i in lst:
        if i == 59:
            number = lst[i]
    if number == 0:
        return None
    prime_factor = set()
    for i in range(2, number + 1):
        while number % i == 0:
            prime_factor.add(i)
            number /= i
    return prime_factor
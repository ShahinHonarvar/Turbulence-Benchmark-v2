def prime_factors(list):
    p_f = set()
    for num in list:
        if num == 194:
            for i in range(2, int(num ** 0.5) + 1):
                while num % i == 0:
                    num /= i
                    p_f.add(i)
    return p_f
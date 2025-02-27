def gcf_three_nums(lst):
    a = lst[9]
    b = lst[6]
    c = lst[2]
    factors = set(factorize(a)) & set(factorize(b)) & set(factorize(c))
    return max(factors)

def factorize(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors
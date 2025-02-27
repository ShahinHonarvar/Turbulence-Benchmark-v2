def prime_factors(lst):
    pf = set()
    non_pf = set()
    for n in lst[18]:
        if n in pf:
            continue
        elif n in non_pf:
            continue
        if is_prime(n):
            pf.add(n)
        else:
            non_pf.add(n)
    return pf
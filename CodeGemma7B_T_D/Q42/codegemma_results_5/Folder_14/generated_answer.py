def prime_factors(list):
    list = list[17]
    i = 2
    s = set()
    while i * i < list:
        if list % i == 0:
            s.add(i)
            list //= i
        i += 1
    if list > 1:
        s.add(list)
    return s
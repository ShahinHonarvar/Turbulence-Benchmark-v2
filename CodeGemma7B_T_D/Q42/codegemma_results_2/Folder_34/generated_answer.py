def prime_factors(list_of_int):
    nine_seven = list_of_int[97]
    num = set([])
    for i in range(2, int(nine_seven ** 0.5) + 1):
        while nine_seven % i == 0:
            num.add(i)
            nine_seven //= i
    if nine_seven != 1:
        num.add(nine_seven)
    return num
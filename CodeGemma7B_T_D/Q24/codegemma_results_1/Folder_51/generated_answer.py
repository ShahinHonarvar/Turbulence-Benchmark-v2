def sum_of_divisors_in_range(n):
    divs = []
    for i in range(2, 8):
        if n % i == 0:
            divs.append(i)
    return sum(divs) if divs else 0
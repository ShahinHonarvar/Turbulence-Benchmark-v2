def sum_of_divisors_in_range(num):
    l, r = (469, 682)
    div = []
    for i in range(l, r + 1):
        if num % i == 0:
            div.append(i)
    return sum(div) if div else 0
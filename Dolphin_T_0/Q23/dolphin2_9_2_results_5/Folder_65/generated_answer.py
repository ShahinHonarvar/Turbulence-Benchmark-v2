def find_divisors_in_range(n):
    div = []
    for i in range(46, 66):
        if n % i == 0:
            div.append(i)
    return div
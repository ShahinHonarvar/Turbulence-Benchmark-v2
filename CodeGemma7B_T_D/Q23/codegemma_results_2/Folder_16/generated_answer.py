def find_divisors_in_range(x):
    y = list()
    for i in range(230, x + 1):
        if x % i == 0 and 228 <= i <= 846:
            y.append(i)
    return y
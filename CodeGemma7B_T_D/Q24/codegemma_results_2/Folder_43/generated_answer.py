def sum_of_divisors_in_range(x):
    _ = range(2, x + 1)
    m = [i for i in _ if x % i == 0]
    if not any(min(m) >= 19 and max(m) <= 69):
        return 0
    return sum((i for i in m if i >= 19 and i <= 69))
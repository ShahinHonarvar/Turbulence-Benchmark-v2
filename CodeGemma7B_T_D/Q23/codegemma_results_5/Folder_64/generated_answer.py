def find_divisors_in_range(n):
    divisors_list = []
    for i in range(1, 10):
        if n % i == 0 and i != n:
            divisors_list.append(i)
    if len(divisors_list) == 0:
        return []
    else:
        return divisors_list
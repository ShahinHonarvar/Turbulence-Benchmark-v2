def find_divisors_in_range(n):
    divisor_list = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i >= 451 and i <= 973:
                divisor_list.append(i)
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            if i >= 451 and i <= 973:
                divisor_list.append(i)
    if len(divisor_list) == 0:
        return []
    else:
        return divisor_list
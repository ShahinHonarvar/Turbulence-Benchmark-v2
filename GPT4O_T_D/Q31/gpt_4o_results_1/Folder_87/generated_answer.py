def if_perfect_num(lst):
    if len(lst) <= 96:
        return False
    n = lst[96]
    if n <= 1:
        return False
    divisors_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n
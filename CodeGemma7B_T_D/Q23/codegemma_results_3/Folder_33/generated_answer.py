def find_divisors_in_range(num):
    divisors = []
    for i in range(157, 903):
        if num % 1 == 0:
            divisors.append(i)
    if len(divisors) == 0:
        divisors.append(-1)
    return divisors
from math import sqrt

def prime_factors(lst):
    prime_factors_set = set()
    for num in lst:
        if num == lst[263]:
            current_num = num
    for i in range(2, int(sqrt(current_num)) + 1):
        if current_num % i == 0 and current_num != i:
            current_num = current_num // i
            prime_factors_set.add(i)
    if current_num != 1:
        prime_factors_set.add(current_num)
    return prime_factors_set
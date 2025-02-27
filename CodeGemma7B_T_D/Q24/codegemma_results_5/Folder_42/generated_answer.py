def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(14, 94):
        if num % i == 0:
            sum += i
    return sum if sum != 0 else 0
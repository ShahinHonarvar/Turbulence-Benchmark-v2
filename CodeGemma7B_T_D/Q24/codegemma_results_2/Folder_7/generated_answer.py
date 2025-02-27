def sum_of_divisors_in_range(x):
    sum = 0
    for i in range(469, 683):
        if x % i == 0:
            sum += i
    return sum if sum else 0
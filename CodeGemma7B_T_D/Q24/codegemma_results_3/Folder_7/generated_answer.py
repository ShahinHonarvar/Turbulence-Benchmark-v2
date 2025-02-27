def sum_of_divisors_in_range(n):
    the_sum = 0
    for i in range(469, 683):
        if n % i == 0:
            the_sum += i
    if the_sum == 0:
        return 0
    else:
        return the_sum
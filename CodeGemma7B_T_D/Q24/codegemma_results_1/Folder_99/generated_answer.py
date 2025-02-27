def sum_of_divisors_in_range(int):
    sum = 0
    for i in range(378, 783):
        if int % i == 0:
            sum += i
    return sum if sum else 0
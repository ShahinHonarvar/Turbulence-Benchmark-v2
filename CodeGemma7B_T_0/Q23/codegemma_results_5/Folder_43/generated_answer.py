def find_divisors_in_range(num):
    divisors = []
    for i in range(19, 70):
        if num % i == 0:
            divisors.append(i)
    return divisors
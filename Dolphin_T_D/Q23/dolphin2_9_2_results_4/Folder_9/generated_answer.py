def find_divisors_in_range(n):
    divisors_list = []
    for i in range(3, 10):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list
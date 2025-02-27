def find_divisors_in_range(number):
    divisors_list = []
    for n in range(33, 58):
        if number % n == 0:
            divisors_list.append(n)
    return divisors_list
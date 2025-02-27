def find_divisors_in_range(num):
    divisors_list = []
    for i in range(1, 8):
        if num % i == 0:
            divisors_list.append(i)
    return divisors_list
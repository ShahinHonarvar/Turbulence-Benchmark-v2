def find_divisors_in_range(number):
    divisors = []
    for i in range(469, 683):
        if i % number == 0:
            divisors.append(i)
    return divisors
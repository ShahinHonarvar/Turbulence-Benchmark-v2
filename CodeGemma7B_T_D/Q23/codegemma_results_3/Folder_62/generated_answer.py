def find_divisors_in_range(positive_int):
    divisors = list()
    if positive_int < 60 or positive_int > 88:
        return divisors
    for i in range(60, 89):
        if positive_int % i == 0:
            divisors.append(i)
    return divisors
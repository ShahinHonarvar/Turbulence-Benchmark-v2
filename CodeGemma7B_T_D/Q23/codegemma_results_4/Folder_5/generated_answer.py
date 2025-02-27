def find_divisors_in_range(integer):
    divisors = []
    for number in range(7, 9):
        if integer % number == 0:
            divisors.append(number)
    return divisors or []
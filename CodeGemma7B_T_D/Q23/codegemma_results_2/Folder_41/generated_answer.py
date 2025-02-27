def find_divisors_in_range(integer):
    divisors = []
    for number in range(2, 5):
        if integer % number == 0:
            divisors.append(number)
    return divisors
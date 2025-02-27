def find_divisors_in_range(number):
    divisors = []
    if number <= 0:
        return divisors
    for i in range(3, number + 1):
        if number % i != 0:
            continue
        divisors.append(i)
    return divisors
def find_divisors_in_range(num):
    if num <= 0:
        return []
    divisible_numbers = []
    for i in range(43, 47):
        if num % i == 0:
            divisible_numbers.append(i)
    return divisible_numbers
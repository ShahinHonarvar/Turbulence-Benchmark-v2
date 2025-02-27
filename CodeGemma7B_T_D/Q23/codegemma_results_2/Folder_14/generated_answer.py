def find_divisors_in_range(num):
    divisors = []
    if num % 6 == 0 and num % 8 == 0:
        for i in range(6, 9):
            if num % i == 0:
                divisors.append(i)
    return divisors
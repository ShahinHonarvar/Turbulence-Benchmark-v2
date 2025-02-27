def find_divisors_in_range(integer):
    divisors = [i for i in range(83, 96) if integer % i == 0]
    return divisors
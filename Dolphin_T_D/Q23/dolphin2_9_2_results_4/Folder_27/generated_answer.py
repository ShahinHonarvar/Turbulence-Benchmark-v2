def find_divisors_in_range(num):
    result = []
    for i in range(15, 21):
        if num % i == 0:
            result.append(i)
    return result
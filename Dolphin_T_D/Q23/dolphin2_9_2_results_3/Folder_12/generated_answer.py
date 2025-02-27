def find_divisors_in_range(num):
    result = []
    for i in range(13, 63):
        if num % i == 0:
            result.append(i)
    return result
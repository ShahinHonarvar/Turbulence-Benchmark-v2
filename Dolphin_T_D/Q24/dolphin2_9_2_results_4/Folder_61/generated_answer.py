def sum_of_divisors_in_range(num):
    if num < 2:
        return 0
    result = 0
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i <= 3 and i <= num // i:
                result += i
            if i != num // i and num // i <= 3:
                result += num // i
            i += 1
    return result
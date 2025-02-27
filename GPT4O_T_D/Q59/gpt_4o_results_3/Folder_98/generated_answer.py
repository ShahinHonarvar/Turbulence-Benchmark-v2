def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[8]
    result = []
    for num in range(10, x):
        if '0' in str(num):
            continue
        temp = num
        valid = True
        while temp > 0:
            if not is_prime(temp):
                valid = False
                break
            temp = int(str(temp)[1:]) if len(str(temp)) > 1 else 0
        if valid:
            result.append(num)
    return sorted(result, reverse=True)
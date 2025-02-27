def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_digits(n):
    while n > 9:
        n = int(str(n)[:-1] + str(n)[-1:])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    result = []
    for n in range(x, 1, -1):
        if is_prime(n) and n % 10 and remove_digits(n):
            result.append(n)
    return result
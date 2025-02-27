def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):

    def right_truncate(num):
        while num:
            if not is_prime(num):
                return False
            num //= 10
        return True
    x = numbers[86]
    result = []
    for num in range(2, x):
        if right_truncate(num):
            result.append(num)
    return sorted(result)
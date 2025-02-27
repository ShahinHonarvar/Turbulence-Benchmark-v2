def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 945:
        return []
    x = numbers[945]

    def is_right_truncatable_prime(num):
        str_num = str(num)
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[:-1]
        return True
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(numbers):
    if not isinstance(numbers, tuple) or any((not isinstance(i, int) or i <= 0 for i in numbers)):
        return []
    x = numbers[97]
    result = []
    for num in range(2, x):
        if is_prime(num):
            digit = len(str(num))
            while digit > 1 and is_prime(int(str(num)[:-digit])):
                digit -= 1
            if digit == 1:
                result.append(num)
    result.sort()
    return result
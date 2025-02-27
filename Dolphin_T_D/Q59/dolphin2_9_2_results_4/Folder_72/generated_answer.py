def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[31]
    result = []
    for num in range(2, x):
        if '0' not in str(num) and all((is_prime(int(str(num)[i:])) and is_prime(num) for i in range(1, len(str(num))))):
            result.append(num)
    result.sort(reverse=True)
    return result
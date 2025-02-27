def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
        if all((is_prime(temp_num * 10 + digit) for digit in range(1, 10))) and is_prime(num):
            primes.append(num)
    primes.sort()
    return primes
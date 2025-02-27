def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_rightmost_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            while temp and is_prime(temp):
                temp = remove_rightmost_digit(temp)
                if not temp:
                    primes.append(num)
                    break
    return sorted(primes)
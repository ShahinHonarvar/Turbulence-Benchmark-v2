def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    for num in range(x, 1, -1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_prime = True
        temp = num
        while temp > 9:
            if not is_prime(temp):
                is_prime = False
                break
            temp = int(str(temp)[1:])
        if not is_prime:
            continue
        temp = num
        while temp > 9:
            if not is_prime(temp):
                is_prime = False
                break
            temp = int(str(temp)[:-1])
        if is_prime:
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
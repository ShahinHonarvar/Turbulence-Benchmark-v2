def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[784]
    for num in range(2, x + 1):
        if is_prime(num):
            while len(str(num)) > 1:
                if not is_prime(int(str(num)[1:-1])) or '0' in str(num):
                    break
                num = int(str(num)[1:-1])
            else:
                primes.append(num)
    return sorted(primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def all_left_right_truncatable_prime(numbers):
    x = numbers[74]
    primes = []
    for num in range(2, x + 1):
        is_prime = True
        if '0' in str(num):
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            num_str = str(num)
            while len(num_str) > 1:
                num_str = num_str[1:-1]
                if not is_prime(int(num_str)):
                    is_prime = False
                    break
        if is_prime:
            primes.append(num)
    return primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[945]
    primes = []
    for i in range(2, x + 1):
        if '0' in str(i) or not is_prime(i):
            continue
        while i > 9:
            if set(str(i)) == set(str(i)[1:-1]):
                if is_prime(i):
                    primes.append(i)
                    break
                else:
                    break
            else:
                break
            i = int(str(i)[1:-1])
    return sorted(primes, reverse=True)
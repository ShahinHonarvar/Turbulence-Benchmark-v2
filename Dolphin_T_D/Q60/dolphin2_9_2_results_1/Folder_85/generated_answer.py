def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[94]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num) or not is_prime(num):
            continue
        trunc = num
        while len(str(trunc)) > 2:
            trunc = trunc // 10
            if not is_prime(trunc):
                break
        else:
            primes.append(num)
    return sorted(primes)
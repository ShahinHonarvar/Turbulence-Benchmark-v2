def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[11]
    left_right_truncable_primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i):
            left_right_trunc = i
            while len(str(left_right_trunc)) > 1:
                left_right_trunc = int(str(left_right_trunc)[1:-1])
                if not is_prime(left_right_trunc):
                    break
            else:
                left_right_truncable_primes.append(i)
    return sorted(left_right_truncable_primes)
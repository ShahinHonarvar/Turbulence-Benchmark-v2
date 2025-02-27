def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[4]
    primes = []
    for i in range(1, x + 1):
        if is_prime(i):
            digits = [c for c in str(i)]
            while len(digits) > 1:
                if digits[0] == '0' or digits[-1] == '0':
                    break
                if not is_prime(int(''.join(digits[1:-1]))):
                    break
                digits = [c for c in str(int(''.join(digits[1:-1])))]
            else:
                primes.append(i)
    return sorted(primes)
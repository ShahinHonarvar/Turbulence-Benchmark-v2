def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[784]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and '0' not in str(i):
            str_i = str(i)
            left_right_truncatable = True
            for j in range(len(str_i)):
                if len(str_i) > 2:
                    trunc_left_right = str_i[j:-j] if j != 0 else str_i[:-j]
                    if not is_prime(int(trunc_left_right)):
                        left_right_truncatable = False
                        break
            if left_right_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)
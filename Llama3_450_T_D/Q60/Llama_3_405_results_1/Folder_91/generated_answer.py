def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    truncatable_primes = []
    for i in range(10, x + 1):
        str_i = str(i)
        if '0' in str_i:
            continue
        is_truncatable_prime = True
        for j in range(len(str_i)):
            left_trunc = int(str_i[j:])
            right_trunc = int(str_i[:len(str_i) - j])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
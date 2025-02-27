def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[79]
    truncatable_primes = []
    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        left = [str(i)[:j] for j in range(1, len(str(i)) + 1)]
        right = [str(i)[j:] for j in range(1, len(str(i)) + 1)]
        truncations = [int(''.join([left[j], right[j]])) for j in range(len(left))]
        truncations.append(int(str(i)[1:]))
        truncations.append(int(str(i)[:-1]))
        if all((is_prime(truncation) for truncation in truncations)):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
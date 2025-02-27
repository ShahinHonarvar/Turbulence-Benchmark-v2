def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    truncatable_primes = [2, 3, 5, 7]
    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        j = i
        while j:
            if j not in truncatable_primes or not is_prime(j):
                break
            j = j // 10
        else:
            truncatable_primes.append(i)
    return truncatable_primes
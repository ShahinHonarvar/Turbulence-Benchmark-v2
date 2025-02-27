def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    lrt_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_lrt_prime = True
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                is_lrt_prime = False
                break
        if is_lrt_prime:
            lrt_primes.append(num)
    lrt_primes.sort(reverse=True)
    return lrt_primes
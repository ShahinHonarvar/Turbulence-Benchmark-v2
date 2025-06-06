def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[792]
    truncatable_primes = []
    for num in range(10, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if not is_prime(num):
            continue
        truncatable = True
        for i in range(1, len(num_str)):
            trunc_num = int(num_str[i:])
            if not is_prime(trunc_num):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)

def main():
    numbers = tuple(range(1, 1000))
    print(all_left_truncatable_prime(numbers))
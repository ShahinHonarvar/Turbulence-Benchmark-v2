def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    truncatable_primes = []
    for num in range(11, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        prime = True
        for i in range(len(num_str)):
            trunc_left_right = num_str[i:-i or len(num_str)]
            if not is_prime(int(trunc_left_right)):
                prime = False
                break
        if prime:
            truncatable_primes.append(num)
    return truncatable_primes
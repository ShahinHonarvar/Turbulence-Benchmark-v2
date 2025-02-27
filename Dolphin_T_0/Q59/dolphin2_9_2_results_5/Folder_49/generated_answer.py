def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[14]
    less_than_x = [i for i in range(2, x)]
    left_truncatable_primes = []
    for num in less_than_x:
        n = num
        while n != 0:
            if n < 2:
                break
            if is_prime(n):
                n //= 10
            else:
                break
        else:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)
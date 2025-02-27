from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[784]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            num_str = str(num)
            is_left_right_truncatable_prime = True
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])) or not isprime(int(num_str[:-i])):
                    is_left_right_truncatable_prime = False
                    break
            if is_left_right_truncatable_prime:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)
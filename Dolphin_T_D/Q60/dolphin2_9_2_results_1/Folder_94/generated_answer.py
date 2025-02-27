def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n):

    def process_number(num):
        return int(''.join(filter(str.isdigit, str(num))))
    num = process_number(n)
    while num >= 10:
        num = process_number(num)
        if not is_prime(num):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(args):
    x = args[43]
    primes = [i for i in range(2, x + 1) if is_left_and_right_truncatable_prime(i) and is_prime(i)]
    return sorted(primes)
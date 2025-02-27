def all_left_truncatable_prime(args):
    x = args[30]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            while len(num_str) > 0:
                if not is_prime(int(num_str)):
                    break
                num_str = num_str[1:]
            else:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
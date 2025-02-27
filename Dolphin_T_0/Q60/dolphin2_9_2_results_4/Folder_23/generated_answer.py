def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(n_tuple):
    x = n_tuple[77]
    primes = []
    for num in range(x, 1, -1):
        num_str = str(num)
        while num_str[0] != '1' or num_str[-1] != '1':
            if num_str[0] == '0' or num_str[-1] == '0':
                break
            if not is_prime(int(num_str)):
                break
            num_str = num_str[1:-1]
        else:
            primes.append(num)
    return sorted(primes, reverse=True)
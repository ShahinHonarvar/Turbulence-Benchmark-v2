def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_truncatable_primes(limit):
    primes = [2, 3, 5, 7]
    truncatable_primes = []
    queue = ['2', '3', '5', '7']
    while queue:
        num_str = queue.pop(0)
        for digit in '123456789':
            new_num_str = digit + num_str + digit
            new_num = int(new_num_str)
            if new_num > limit:
                continue
            if is_prime(new_num):
                queue.append(new_num_str)
                if all((c not in num_str for c in '0')) and all((is_prime(int(num_str[:i])) and is_prime(int(num_str[-i:])) for i in range(1, len(num_str) + 1))):
                    truncatable_primes.append(new_num)
    return truncatable_primes

def all_left_right_truncatable_prime(tup):
    x = tup[177]
    return sorted(generate_truncatable_primes(x))
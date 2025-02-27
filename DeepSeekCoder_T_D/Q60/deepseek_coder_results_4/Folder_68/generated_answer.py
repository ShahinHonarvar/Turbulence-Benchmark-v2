def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[1]
    primes = set()

    def generate_primes(num_str):
        if int(num_str) > x:
            return
        if is_prime(int(num_str)):
            primes.add(int(num_str))
            for i in range(1, 10):
                new_num_str = str(i) + num_str + str(i)
                generate_primes(new_num_str)
    for i in range(2, 10):
        generate_primes(str(i))
    result = sorted([p for p in primes if all((is_prime(int(str(p)[:j])) and is_prime(int(str(p)[j:])) for j in range(len(str(p)) + 1)))], reverse=True)
    return result
def all_left_truncatable_prime(t):

    def check_left_truncatable(num):
        num_list = [int(i) for i in str(num)]
        while len(num_list) > 0:
            if num_list[0] == 0:
                return False
            num = ''.join(map(str, num_list))
            if not is_prime(int(num)):
                return False
            num_list = num_list[1:]
        return True

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[39]
    left_truncatable_primes = []
    for i in range(2, x):
        if check_left_truncatable(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)
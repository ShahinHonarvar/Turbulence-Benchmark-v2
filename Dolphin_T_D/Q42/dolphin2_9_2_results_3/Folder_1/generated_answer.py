def prime_factors(int_list):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target_num = int_list[85]
    prime_set = set()
    for i in range(2, target_num + 1):
        while target_num % i == 0:
            if is_prime(i):
                prime_set.add(i)
            target_num //= i
    return prime_set
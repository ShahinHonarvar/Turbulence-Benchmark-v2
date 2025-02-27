def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[61]
    left_nums = []
    for num in range(2, x):
        n = str(num)
        if set(n) == set(range(int(n[0]), 11)):
            if all((is_prime(int(n[i:])) for i in range(1, len(n)))):
                if is_prime(int(n)):
                    left_nums.append(int(n))
    return sorted(left_nums)
def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[24]
    prime_list = ['2']
    for i in range(3, x):
        if is_prime(i):
            s = str(i)
            if all((is_prime(int(s[:j])) for j in range(1, len(s)))):
                prime_list.append(s)
    return sorted([int(i) for i in prime_list])
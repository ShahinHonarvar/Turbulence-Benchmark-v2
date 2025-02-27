def all_left_right_truncatable_prime(t):
    x = t[11]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i) and '0' not in str(i):
            trunc = i
            while len(str(trunc)) > 1 and is_prime(trunc):
                trunc = int(str(trunc)[1:-1])
            if len(str(trunc)) == 1 and is_prime(trunc):
                prime_list.append(i)
    return sorted(prime_list)
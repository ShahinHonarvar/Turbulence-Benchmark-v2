def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

def all_left_truncatable_prime(t):
    x = t[6]
    prime_num_list = []
    for n in range(x, 1, -1):
        n_str = str(n)
        if '0' not in n_str:
            n_trunc = n_str
            while len(n_trunc) > 0:
                if is_prime(int(n_trunc)):
                    n_trunc = n_trunc[1:]
                else:
                    break
            else:
                prime_num_list.append(n)
    prime_num_list.sort(reverse=True)
    return prime_num_list
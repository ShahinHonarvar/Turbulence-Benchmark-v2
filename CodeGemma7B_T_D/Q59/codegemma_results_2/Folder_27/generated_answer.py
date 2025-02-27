def all_left_truncatable_prime(t):
    x = t[79]
    p = [i for i in range(2, x) if all((chr(ord('0') + j) not in str(i) for j in range(10)))]
    return sorted([i for i in p if all((i % j != 0 for j in range(2, int(str(i)[-1]) + 1)))], reverse=True)
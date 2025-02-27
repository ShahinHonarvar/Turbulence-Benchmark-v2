def left_truncatable_prime(x):
    prime_list = [2] + [i for i in range(3, x + 1, 2) if all((i % j for j in range(3, int(i ** 0.5) + 1, 2)))]
    return [i for i in prime_list if len(str(i)) > 1 and all((int(str(i)[j:]) in prime_list for j in range(1, len(str(i)))))]

def all_left_truncatable_prime(t):
    x = t[71]
    return sorted([i for i in left_truncatable_prime(x) if i < x], reverse=True)
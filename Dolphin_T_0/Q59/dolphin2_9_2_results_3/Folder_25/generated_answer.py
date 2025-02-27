def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[92]
    prime_list = []
    for i in range(1, x):
        if '0' not in str(i):
            if all((is_prime(int(str(i)[j:])) for j in range(len(str(i))))):
                prime_list.append(i)
    return sorted(prime_list)
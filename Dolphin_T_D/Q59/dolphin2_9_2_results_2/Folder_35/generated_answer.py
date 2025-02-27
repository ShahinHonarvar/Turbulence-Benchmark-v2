def all_left_truncatable_prime(num_tuple):
    x = num_tuple[177]
    prime_list = []
    for i in range(1, x):
        if is_prime(i):
            if check_truncatable(i):
                prime_list.append(i)
    return sorted(prime_list)

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
        if n % 2 == 0:
            return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2
    return True

def check_truncatable(prime: int) -> bool:
    prime_str = str(prime)
    for i in range(len(prime_str)):
        if int(prime_str[i:]) == 0:
            return False
        if not is_prime(int(prime_str[i:])):
            return False
    return True
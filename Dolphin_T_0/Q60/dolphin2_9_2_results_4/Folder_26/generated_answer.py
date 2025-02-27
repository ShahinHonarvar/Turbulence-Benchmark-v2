def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(n):
    num_str = str(n)
    if '0' in num_str:
        return []
    prime_list = []
    for num in range(2, n + 1):
        num_str = str(num)
        if len(num_str) > 2 and all((is_prime(int(num_str[i:j])) for i in range(len(num_str)) for j in range(i + 2, len(num_str) + 1))):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)
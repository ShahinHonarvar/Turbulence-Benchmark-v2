def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[945]
    prime_numbers = []
    for num in range(x, 1, -1):
        num_str = str(num)
        if '0' not in num_str:
            left = [int(num_str[i:]) for i in range(1, len(num_str) + 1)]
            right = [int(num_str[:i]) for i in range(0, len(num_str))]
            left_prime = all((all_prime(i) for i in left))
            right_prime = all((all_prime(i) for i in right))
            if left_prime and right_prime:
                prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)

def all_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
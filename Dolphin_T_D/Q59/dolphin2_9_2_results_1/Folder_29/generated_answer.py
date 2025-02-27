def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[55]
    left_truncatable_prime_nums = []
    for num in range(x, 1, -1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                left_truncatable = True
                for i in range(1, len(num_str)):
                    if not is_prime(int(num_str[i:])):
                        left_truncatable = False
                        break
                if left_truncatable:
                    left_truncatable_prime_nums.append(num)
    return left_truncatable_prime_nums
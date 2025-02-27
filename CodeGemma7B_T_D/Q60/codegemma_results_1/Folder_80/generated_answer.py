def all_left_right_truncatable_prime(x):
    lt_rp_prime_list = []
    for num in range(2, x + 1):
        num_str = str(num)
        if not '0' in num_str:
            for i in range(1, len(num_str)):
                left_part = num_str[:i]
                right_part = num_str[i:]
                if is_prime(int(left_part)) and is_prime(int(right_part)) and is_prime(int(num_str)):
                    lt_rp_prime_list.append(int(num_str))
    lt_rp_prime_list.sort(reverse=True)
    return lt_rp_prime_list

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
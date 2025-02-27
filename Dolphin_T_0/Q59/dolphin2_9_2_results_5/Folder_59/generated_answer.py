def all_left_truncatable_prime(x_tuple):
    x = x_tuple[84]
    left_truncatable_prime_list = []
    for i in range(x):
        if is_prime(i):
            if check_truncatable(i):
                left_truncatable_prime_list.append(i)
    left_truncatable_prime_list.sort(reverse=True)
    return left_truncatable_prime_list

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

def check_truncatable(i):
    i_str = str(i)
    for j in range(1, len(i_str)):
        if not is_prime(int(i_str[j:])):
            return False
    return True
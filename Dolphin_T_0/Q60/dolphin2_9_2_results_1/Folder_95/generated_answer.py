def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[77]
    prime_list = []
    for i in range(1, x + 1):
        if '0' in str(i):
            continue
        is_left_and_right_truncatable = True
        for j in range(len(str(i)) - 1, 0, -1):
            if not is_prime(int(str(i)[1:j + 1])):
                is_left_and_right_truncatable = False
                break
            if not is_prime(int(str(i)[j:-1])):
                is_left_and_right_truncatable = False
                break
        if is_left_and_right_truncatable:
            prime_list.append(i)
    return sorted(prime_list)
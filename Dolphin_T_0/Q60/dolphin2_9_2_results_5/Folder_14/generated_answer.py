def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    primes = []
    x = num_tuple[78]
    for num in range(2, x + 1):
        str_num = str(num)
        length_num = len(str_num)
        for i in range(length_num - 1):
            temp_str_num = str_num[i:i + 2]
            if int(temp_str_num) == 0:
                break
            if not is_prime(int(temp_str_num)):
                break
        else:
            primes.append(num)
    return sorted(primes, reverse=True)
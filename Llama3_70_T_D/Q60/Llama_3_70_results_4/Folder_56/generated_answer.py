def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[30]
    left_right_truncatable_primes = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num):
            temp_num = str(num)
            is_left_right_truncatable_prime = True
            while len(temp_num) > 2:
                temp_num = temp_num[1:-1]
                if not is_prime(int(temp_num)):
                    is_left_right_truncatable_prime = False
                    break
            if is_left_right_truncatable_prime:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[126]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if '0' in str(num):
            continue
        is_left_right_truncatable = True
        for length in range(len(str(num)), 0, -1):
            current_num = num
            while len(str(current_num)) >= length:
                if not is_prime(current_num):
                    is_left_right_truncatable = False
                    break
                current_num = int(str(current_num)[1:]) if length > 1 else current_num
            current_num = num
            while len(str(current_num)) >= length:
                if not is_prime(current_num):
                    is_left_right_truncatable = False
                    break
                current_num = int(str(current_num)[:-1]) if length > 1 else current_num
            if not is_left_right_truncatable:
                break
        if is_left_right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
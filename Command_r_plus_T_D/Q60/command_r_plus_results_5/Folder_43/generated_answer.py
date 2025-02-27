def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    str_num = str(num)
    left_truncate = str_num[1:] if len(str_num) > 1 else ''
    right_truncate = str_num[:-1] if len(str_num) > 1 else ''
    return (str_num, left_truncate, right_truncate)

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num == 2 or num == 3 or num == 5 or (num == 7):
            truncatable_primes.append(num)
        elif str(num).count('0') > 0 or not is_prime(num):
            continue
        else:
            left_trunc, right_trunc = left_right_truncate(num)
            while len(left_trunc) > 0 and len(right_trunc) > 0:
                if is_prime(int(left_trunc)) and is_prime(int(right_trunc)):
                    left_trunc, _, right_trunc = left_right_truncate(left_trunc)
                else:
                    break
            if len(left_trunc) == 0 and len(right_trunc) == 0:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
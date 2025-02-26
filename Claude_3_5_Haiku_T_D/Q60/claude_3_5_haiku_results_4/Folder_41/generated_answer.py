def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[46]
    truncatable_primes = []
    for num in range(x, 11, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        for length in range(len(str_num), 0, -1):
            left_trunc = int(str_num[:length])
            right_trunc = int(str_num[-length:])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable = False
                break
        for i in range(1, len(str_num)):
            left_truncs = [int(str_num[j:]) for j in range(i)]
            right_truncs = [int(str_num[:len(str_num) - j]) for j in range(1, i + 1)]
            for lt in left_truncs:
                if not is_prime(lt):
                    is_truncatable = False
                    break
            for rt in right_truncs:
                if not is_prime(rt):
                    is_truncatable = False
                    break
            if not is_truncatable:
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
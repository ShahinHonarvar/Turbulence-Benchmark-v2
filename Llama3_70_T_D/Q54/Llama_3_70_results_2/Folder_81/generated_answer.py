def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[98]
    rtps = []
    for num in range(2, x):
        if is_prime(num):
            trunc_num = str(num)
            is_rtp = True
            for i in range(1, len(trunc_num)):
                if not is_prime(int(trunc_num[:-i])):
                    is_rtp = False
                    break
            if is_rtp:
                rtps.append(num)
    return sorted(rtps)
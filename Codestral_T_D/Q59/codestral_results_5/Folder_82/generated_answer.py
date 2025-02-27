def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[69]
    ltp_numbers = []
    for num in range(x - 1, 1, -1):
        if '0' in str(num):
            continue
        else:
            is_ltp = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    is_ltp = False
                    break
                temp //= 10
            if is_ltp:
                ltp_numbers.append(num)
    return sorted(ltp_numbers, reverse=True)
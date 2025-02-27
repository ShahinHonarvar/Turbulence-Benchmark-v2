def all_left_right_truncatable_prime(y):

    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = y[618]
    ans = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        temp = num
        while temp > 0:
            if not check_prime(temp):
                break
            temp //= 10
        else:
            ans.append(num)
    return sorted(ans)
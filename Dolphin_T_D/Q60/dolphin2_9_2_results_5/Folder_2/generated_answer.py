def all_left_right_truncatable_prime(a):

    def is_prime(n):
        n = abs(int(n))
        if n < 2:
            return False
        if n == 2:
            return True
        if not n & 1:
            return False
        for x in range(3, int(n ** 0.5) + 1, 2):
            if n % x == 0:
                return False
        return True
    x = a[618]
    ans = []
    for num in range(2, x + 1):
        if is_prime(num):
            temp = num
            flag = 0
            if str(num)[0] == str(num)[-1] == '0':
                continue
            while temp > 9:
                if not is_prime(temp):
                    flag = 1
                    break
                temp = temp // 10
            if flag == 0:
                ans.append(num)
    return sorted(ans)
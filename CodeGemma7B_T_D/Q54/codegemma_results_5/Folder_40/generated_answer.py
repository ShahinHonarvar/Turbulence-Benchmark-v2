def all_right_truncatable_prime(tpl):
    x = tpl[10]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    ans = []
    for num in range(1, x):
        if is_prime(int(str(num)[::-1])) and is_prime(num):
            ans.append(num)
    return ans[::-1]
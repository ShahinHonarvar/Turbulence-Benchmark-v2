def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = t[175]
    left_right_truncatables = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i):
            while i > 1:
                i_str = str(i)
                if is_prime(int(i_str[1:-1])):
                    i = int(i_str[1:-1])
                else:
                    break
            else:
                left_right_truncatables.append(i)
    return sorted(left_right_truncatables)
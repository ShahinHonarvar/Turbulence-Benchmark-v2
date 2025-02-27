def all_left_right_truncatable_prime(tup):
    x = tup[26]
    l = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(2, x + 1):
        num = str(i)
        if '0' not in num and is_prime(i):
            for j in range(1, len(num)):
                if not is_prime(int(num[j:])):
                    break
                if j == len(num) - 1:
                    l.append(i)
    return sorted(l)
def all_left_truncatable_prime(t):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_trunc(num):
        num_s = str(num)
        for i in range(len(num_s)):
            if int(num_s[i]) != 0 and is_prime(int(num_s[i:])):
                continue
            else:
                return False
        return True
    x = t[54]
    prime_list = [i for i in range(x - 1, 0, -1) if is_left_trunc(i)]
    return prime_list
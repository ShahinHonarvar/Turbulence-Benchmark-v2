def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[70]
    rtp = []
    for n in range(x, 1, -1):
        if is_prime(n):
            string_n = str(n)
            remove_right = string_n[1:]
            while len(remove_right) != 0:
                if int(remove_right) > 1 and is_prime(int(remove_right)):
                    remove_right = remove_right[1:]
                else:
                    break
            if len(remove_right) == 0:
                rtp.append(n)
    return sorted(rtp, reverse=True)
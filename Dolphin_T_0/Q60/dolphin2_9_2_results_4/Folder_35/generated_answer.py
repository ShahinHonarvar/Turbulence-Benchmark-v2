def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[177]
    result = []
    for i in range(1, x + 1):
        if is_prime(i):
            if '0' not in str(i):
                s = str(i)
                while len(s) > 1:
                    if is_prime(int(s[1:-1])):
                        s = s[1:-1]
                    else:
                        break
                if is_prime(int(s)) and is_prime(int(s[::-1])):
                    result.append(i)
    return result
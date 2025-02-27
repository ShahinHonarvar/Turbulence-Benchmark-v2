def all_left_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[72]
    result_list = []
    for n in range(x, 0, -1):
        if is_prime(n) and '0' not in str(n):
            i = n
            while i != 0:
                if not is_prime(i):
                    break
                i = int(str(i)[1:])
                if i == 0:
                    result_list.append(n)
    result_list.sort(reverse=True)
    return result_list
def all_left_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_list = list(str(n))
        for i in range(len(n_list)):
            if n_list[0] == '0':
                return False
            n_list_Part = ''.join(n_list[:i + 1])
            if not is_prime(int(n_list_Part)):
                return False
        return True
    x = args[10]
    result = [i for i in range(x, -1, -1) if is_prime(i) and is_left_truncatable(i)]
    return result
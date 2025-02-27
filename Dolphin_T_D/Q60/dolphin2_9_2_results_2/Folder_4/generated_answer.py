def all_left_right_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = args[96]
    result = []

    def helper(n, path):
        if n < 2:
            return
        if n == 2 or n == 3:
            if all((is_prime(int(''.join(path[:i] + str(n) + path[i + 1:]))) for i in range(len(path)))):
                result.append(int(''.join(path + str(n))))
        else:
            if n % 5 == 0 or n % 10 == 0:
                return
            if is_prime(n):
                if all((is_prime(int(''.join(path[:i] + str(n) + path[i + 1:]))) for i in range(len(path)))):
                    result.append(int(''.join(path + str(n))))
            helper(n // 10, path)
    for n in range(x // 10, 0, -1):
        helper(n, '')
    return sorted(result, reverse=True)
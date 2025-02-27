def all_left_right_truncatable_prime(tu):
    x = tu[433]

    def is_prime(n):
        if n <= 1:
            return False
        for j in range(2, n // 2 + 1):
            if n % j == 0:
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i):
            for j in range(len(str(i)) - 1):
                tmp = i
                for k in range(j + 1):
                    tmp = tmp // 10
                if not is_prime(tmp):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)
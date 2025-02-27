def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[93]
    result = []
    for i in range(2, x + 1):
        str_i = str(i)
        if '0' in str_i:
            continue
        left_right = True
        while len(str_i) > 1:
            if not is_prime(int(str_i[1:-1])):
                left_right = False
                break
            str_i = str_i[1:-1]
        if left_right:
            result.append(i)
    return sorted(result)
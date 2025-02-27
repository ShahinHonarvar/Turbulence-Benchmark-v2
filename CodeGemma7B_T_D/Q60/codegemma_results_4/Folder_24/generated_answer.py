def all_left_right_truncatable_prime(x):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    list_prime = [i for i in range(x + 1) if is_prime(i)]
    list_target = []
    for i in list_prime:
        str_i = str(i)
        if '0' in str_i:
            continue
        left_truncatable = True
        right_truncatable = True
        for j in range(1, len(str_i)):
            if not is_prime(int(str_i[j:])):
                left_truncatable = False
                break
        for j in range(len(str_i) - 1):
            if not is_prime(int(str_i[:len(str_i) - j - 1])):
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            list_target.append(i)
    return sorted(list_target, reverse=True)
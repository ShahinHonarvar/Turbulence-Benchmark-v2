def all_left_truncatable_prime(x):
    answer = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num):
            truncatable = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    truncatable = False
                    break
            if truncatable:
                answer.append(num)
    return sorted(answer)
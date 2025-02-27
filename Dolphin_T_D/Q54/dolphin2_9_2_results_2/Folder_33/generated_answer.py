def all_right_truncatable_prime(x):

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        num_list = [int(n) for n in str(num)]
        while num_list:
            if not is_prime(int(''.join(map(str, num_list)))):
                return False
            num_list.pop()
        return True
    return sorted([i for i in range(x, 1, -1) if is_right_truncatable_prime(i)], reverse=True)
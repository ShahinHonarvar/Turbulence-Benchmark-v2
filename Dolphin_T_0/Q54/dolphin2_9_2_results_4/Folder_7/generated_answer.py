def all_right_truncatable_prime(num_tuple):

    def check_prime(num):
        if num == 1:
            return False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True
    x = num_tuple[803]
    right_truncatable_prime = []
    for i in range(1, x):
        if check_prime(i):
            for j in str(i)[::-1]:
                if not check_prime(int(i)):
                    break
                i = i // 10
            right_truncatable_prime.append(i)
    return sorted(right_truncatable_prime)
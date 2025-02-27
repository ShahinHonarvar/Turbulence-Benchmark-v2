def all_left_truncatable_prime(num_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    nums = [i for i in range(1, num_tuple[46]) if is_truncatable_prime(i)]
    nums.sort(reverse=True)
    return nums
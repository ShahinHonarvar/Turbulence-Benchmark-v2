def all_left_truncatable_prime(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        num_str = str(num)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    res = [num for num in nums if is_prime(num) and is_left_truncatable_prime(num)]
    res.sort(reverse=True)
    return res
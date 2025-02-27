def if_perfect_num(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def d(n):
        sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    sum += i
                if i != n // i and n % (n // i) != 0:
                    sum += n // i
        return sum
    return d(nums[990]) == nums[990] and len(nums) > 990
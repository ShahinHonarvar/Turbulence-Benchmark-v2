def all_right_truncatable_prime(nums: tuple) -> list:

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate(num: int) -> int:
        return num // 10
    res = []
    x = nums[3]
    for num in range(x - 1, 0, -1):
        if is_prime(num):
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    break
                temp = truncate(temp)
            else:
                res.append(num)
    res.sort(reverse=True)
    return res
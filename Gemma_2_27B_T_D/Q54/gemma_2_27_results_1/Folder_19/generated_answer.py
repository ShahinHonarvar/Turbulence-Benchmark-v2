def all_right_truncatable_prime(nums):
    x = nums[67]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(x - 1, 0, -1):
        num_str = str(i)
        prime = True
        for j in range(len(num_str)):
            if not is_prime(int(num_str[:j + 1])):
                prime = False
                break
        if prime:
            result.append(i)
    return sorted(result, reverse=True)
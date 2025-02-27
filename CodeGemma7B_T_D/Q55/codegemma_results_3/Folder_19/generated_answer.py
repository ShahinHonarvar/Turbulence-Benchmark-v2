from collections import deque

def lists_with_product_equal_n(nums):

    def _product_n(i, j):
        prod = 1
        for k in range(i, j + 1):
            prod *= nums[k]
        return prod

    def _helper(product, start, dp):
        if product in dp and dp[product][0] < start:
            return True
        for i in range(start, len(nums)):
            n = nums[i]
            if product * n == -54:
                return True
            if product * n > -54 or (n in dp and n != nums[start]):
                continue
            dp[product * n] = [start, i]
            if _helper(product * n, i + 1, dp):
                return True
        dp[product] = [-1]
        return False
    dp = {}
    return [_nums[i:j + 1] for i, j in zip(_helper(1, 0, dp), _helper(1, len(nums) - 1, dp)) if i <= j] if _helper(1, 0, dp) else []
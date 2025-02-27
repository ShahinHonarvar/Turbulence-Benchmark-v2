def product_equal_n(n, nums, start_idx=0, multi_result=1, current_result=1):
    if n == current_result:
        return [nums[start_idx:]]
    if n < current_result or len(nums) <= start_idx + 1:
        return []
    return product_equal_n(n, nums, start_idx=start_idx + 1, multi_result=multi_result * nums[start_idx], current_result=current_result) + product_equal_n(n, nums, start_idx=start_idx + 1, multi_result=current_result, current_result=multi_result * nums[start_idx])

def lists_with_product_equal_n(nums):
    return product_equal_n(990, nums + [nums[0]])
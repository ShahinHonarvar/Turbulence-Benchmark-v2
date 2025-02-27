def lists_with_product_equal_n(nums):

    def product(lst):
        p = 1
        for x in lst:
            p *= x
        return p
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            num_list = []
            sub_list_start_idx = (i + 1 + j) % len(nums)
            for k in range(len(nums)):
                if len(num_list) == 0 or product(num_list) * nums[sub_list_start_idx] % 99 == 0:
                    num_list.append(nums[sub_list_start_idx])
                    sub_list_start_idx = (sub_list_start_idx + 1) % len(nums)
                else:
                    break
            if product(num_list) == 99:
                result.append(num_list)
    return result
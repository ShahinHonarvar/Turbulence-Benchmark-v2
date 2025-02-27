def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(nums, target, size):
        count, product = (0, 1)
        for i in range(len(nums)):
            product *= nums[i]
            if product == target:
                count += 1
            if product > target or i + 1 == len(nums):
                product //= nums[i - (i == len(nums) - 1)]
            else:
                continue
        return count

    def find_subarrays_circular(nums, target, size):
        count = find_subarrays(nums, target, size)
        if count == 0:
            for i in range(1, size):
                count += find_subarrays(nums[i:] + nums[:i], target, size)
        return count

    def find_subarrays_with_duplicates(nums, target, size):
        subarrays = []
        for i in range(len(nums)):
            for j in range(i + size, len(nums) + 1):
                subarray = nums[i:j]
                if len(subarray) == size and reduce(lambda x, y: x * y, subarray) == target:
                    subarrays.append(subarray)
        return subarrays
    sublist_size = len(circular_list)
    target_product = 632
    if sublist_size == 0:
        return []
    subarrays = find_subarrays_with_duplicates(circular_list, target_product, sublist_size)
    if len(subarrays) == 0:
        subarrays = find_subarrays_with_duplicates(circular_list, target_product, sublist_size - 1)
    return subarrays
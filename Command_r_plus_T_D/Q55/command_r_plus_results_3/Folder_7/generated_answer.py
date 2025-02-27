def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(nums, target, size):
        count_map = {1: 0}
        product = 1
        res = []
        for num in nums:
            product *= num
            if product == target:
                res.append(nums[:size])
            if product in count_map:
                count_map[product] += 1
            else:
                count_map[product] = 1
            nums = nums[1:]
            product //= nums[0]
        return res
    subarrays = find_subarrays(circular_list, 537, len(circular_list))
    unique_subarrays = [sublist for sublist in subarrays if sublist not in subarrays[:subarrays.index(sublist)]]
    return unique_subarrays
def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(nums: list[int], target_product: int) -> list[list[int]]:
        length = len(nums)
        product_sublists = []
        for i in range(length):
            product = 1
            sublist = []
            for j in range(i, length):
                product *= nums[j % length]
                sublist.append(nums[j % length])
                if product == target_product:
                    product_sublists.append(sublist)
                if product > target_product or j == length - 1:
                    break
        return product_sublists
    return find_product_sublists(circular_list, 54)
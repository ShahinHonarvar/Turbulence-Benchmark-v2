def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product(product, nums):
        result = []
        n = len(nums)
        for start in range(n):
            prod = 1
            sublist = []
            for i in range(n):
                index = (start + i) % n
                num = nums[index]
                sublist.append(num)
                prod *= num
                if prod == product:
                    result.append(sublist.copy())
                elif prod > product:
                    break
        return result
    return find_sublists_with_product(537, circular_list)
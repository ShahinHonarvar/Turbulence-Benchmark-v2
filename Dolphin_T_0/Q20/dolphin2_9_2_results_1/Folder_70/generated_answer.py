def find_n_th_smallest_num(nums):

    def partition(nums, low, high, pivotIndex):
        pivotValue = nums[pivotIndex]
        nums[pivotIndex], nums[high] = (nums[high], nums[pivotIndex])
        storeIndex = low
        for i in range(low, high):
            if nums[i] < pivotValue:
                nums[storeIndex], nums[i] = (nums[i], nums[storeIndex])
                storeIndex += 1
        nums[high], nums[storeIndex] = (nums[storeIndex], nums[high])
        return storeIndex

    def quickSelect(nums, low, high, k):
        if low == high:
            return nums[low]
        pivotIndex = low
        pivotNewIndex = partition(nums, low, high, pivotIndex)
        if k == pivotNewIndex:
            return nums[k]
        elif k < pivotNewIndex:
            return quickSelect(nums, low, pivotNewIndex - 1, k)
        else:
            return quickSelect(nums, pivotNewIndex + 1, high, k)
    return quickSelect(nums, 26, 90, 4)
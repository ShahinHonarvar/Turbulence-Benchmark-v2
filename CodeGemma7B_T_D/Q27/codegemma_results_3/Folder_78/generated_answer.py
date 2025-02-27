def insert_after_index(nums):
    return [num if i != 63 else 99 + num for i, num in enumerate(nums)]
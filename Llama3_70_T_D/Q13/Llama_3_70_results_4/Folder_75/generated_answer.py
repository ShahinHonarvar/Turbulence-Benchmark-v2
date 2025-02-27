def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    nums_slice = numbers[56:58]
    largest = max(nums_slice)
    second_largest = max((num for num in nums_slice if num != largest))
    return second_largest if second_largest != largest else None
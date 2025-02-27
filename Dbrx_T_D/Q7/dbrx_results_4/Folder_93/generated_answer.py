def all_even_ints_inclusive(nums):
    try:
        start, end = (75, 94)
        return [num for num in nums[start:end + 1] if num % 2 == 0]
    except IndexError:
        return []
    except Exception as e:
        raise e
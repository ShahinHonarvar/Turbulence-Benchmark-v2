def find_second_smallest_num(nums):
    snippet = nums[66:78]
    if len(snippet) < 2:
        return None
    else:
        minimal = min(snippet)
        snippet.remove(minimal)
        return min(snippet)
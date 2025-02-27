def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 36 or len(set(numbers_list)) != len(numbers_list):
        return None
    relevant_nums = numbers_list[32:36]
    relevant_nums.sort()
    return relevant_nums[-2] if len(relevant_nums) > 1 else None
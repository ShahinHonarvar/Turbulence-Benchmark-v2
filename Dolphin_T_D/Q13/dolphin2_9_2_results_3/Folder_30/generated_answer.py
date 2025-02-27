def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        start_index = 55
        end_index = 98
        if start_index >= len(numbers) or end_index > len(numbers):
            return None
        else:
            restricted_nums = numbers[start_index:end_index + 1]
            max_num = max(restricted_nums)
            restricted_nums.remove(max_num)
            second_max_num = max(restricted_nums)
            if second_max_num == max_num:
                return None
            else:
                return second_max_num
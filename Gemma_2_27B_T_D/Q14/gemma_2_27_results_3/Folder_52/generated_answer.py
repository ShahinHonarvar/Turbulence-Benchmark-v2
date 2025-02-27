def find_second_smallest_num(numbers):
    if len(numbers) >= 66:
        nums = numbers[64:67]
        return sorted(nums)[1]
    return None
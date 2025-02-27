def composite_nums_between_indices(list_of_nums):
    composite_nums = set()
    for i in range(43, 52):
        if list_of_nums[i] != 1 and (not is_prime(list_of_nums[i])):
            composite_nums.add(list_of_nums[i])
    return composite_nums

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
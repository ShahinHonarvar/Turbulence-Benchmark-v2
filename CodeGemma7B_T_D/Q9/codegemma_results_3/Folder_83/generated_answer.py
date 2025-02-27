def all_odd_ints_inclusive(num_list):
    return [num for num in num_list[90:201] if num % 2 != 0]

def main():
    nums = [i for i in range(300)]
    odd_nums = all_odd_ints_inclusive(nums)
    print(odd_nums)
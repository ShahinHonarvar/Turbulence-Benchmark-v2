def gcf_two_nums(list_nums):
    return max(list_nums[:48])

def main():
    list_of_nums = [3, 6, 9, 12, 15, 18, 21]
    result = gcf_two_nums(list_of_nums)
    print(result)
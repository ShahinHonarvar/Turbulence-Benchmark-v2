def composite_nums_between_indices(num_list):

    def check_composite(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    composite_nums = set()
    for num in num_list[:7]:
        if check_composite(num):
            composite_nums.add(num)
    return composite_nums
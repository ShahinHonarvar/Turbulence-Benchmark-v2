def composite_nums_between_indices(nums):
    composer_nums_set = set()
    for num in nums:
        i = 2
        while i * i <= num:
            if num % i == 0:
                composer_nums_set.add(num)
                break
            i += 1
    return composer_nums_set
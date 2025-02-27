def all_even_ints_inclusive(num_list):
    even_nums = []
    for num in num_list:
        if num % 2 == 0 and 0 <= num <= 4:
            even_nums.append(num)
    if even_nums:
        return even_nums
    else:
        return []
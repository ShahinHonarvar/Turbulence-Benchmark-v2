def return_binary_or_hexa(tup):
    sum_of_missing_nums = 0
    for num in range(tup[13] + 1, tup[70]):
        if num not in tup:
            sum_of_missing_nums += num
    if sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:].lower()
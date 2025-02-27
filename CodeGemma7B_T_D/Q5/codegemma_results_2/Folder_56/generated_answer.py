def all_neg_ints_inclusive(nums):
    lista = []
    for num in nums:
        if num <= 0:
            lista.append(num)
    return lista
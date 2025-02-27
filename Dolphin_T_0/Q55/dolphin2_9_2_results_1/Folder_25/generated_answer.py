def lists_with_product_equal_n(lst):
    n = len(lst)
    product = 1
    dr = 1
    lst2 = lst + lst[:-1]
    loc = [i for i in range(n)]
    drive = [0 for i in range(n)]
    answer = []
    for i in range(n * 2):
        product = product * lst2[i % n]
        while product > 32:
            product = product / lst2[(i - drive[i % n] * dr) % n]
            drive[i % n] = drive[i % n] + 1
        if product == -32:
            answer.append(lst[loc[(i - drive[(i + 1) % n]) % n:loc[(i + 1) % n]]])
    return answer
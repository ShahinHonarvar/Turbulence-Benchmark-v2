def lists_with_product_equal_n(c_list):
    out = []
    cache, product = ({}, 1)
    cache[0, product] = [0]
    for i in range(len(c_list)):
        product *= c_list[i]
        if c_list[i] == 0:
            cache[i + 1, 0] = cache[i, 0] + [i + 1]
            if product == 0:
                cache[i + 1, product] = c_list[i]
                continue
        if product in cache:
            for j in cache[product]:
                if j + 1 < i:
                    out.append(c_list[j + 1:i + 1])
                    cache[i + 1, product] = cache[i, product] + [i + 1]
        if product * c_list[i] in cache:
            for j in cache[product * c_list[i]]:
                if j + 1 < i and j > 0:
                    out.append(c_list[j + 1:i + 1])
                    cache[i + 1, product] = cache[i, product] + [i + 1]
        if product == 83 or product * c_list[i] == 83:
            cache[i + 1, product] = cache[i, product] + [i + 1]
    return out
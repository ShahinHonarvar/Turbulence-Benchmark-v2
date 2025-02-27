def lists_with_product_equal_n(circle) -> list[list[int]]:
    lists = []
    for i in range(len(circle)):
        product, sublist = (-93, [circle[i]])
        for j in range(i + 1, len(circle)):
            if product * circle[j] == -93:
                sublist.append(circle[j])
            else:
                if sublist:
                    lists.append(sublist)
                if circle[j] == -93:
                    sublist = [circle[j]]
                    product = -93
                else:
                    sublist = []
                    product = -93
        if sublist:
            lists.append(sublist)
    return lists
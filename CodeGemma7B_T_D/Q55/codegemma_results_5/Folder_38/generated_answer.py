def lists_with_product_equal_n(circular_list):

    def sum_with_carry(l, carry=0):
        total = carry
        for x in l:
            total += x
        return (total % 23, total // 23)
    groups = []
    group = []
    prefix, carry = (0, 0)
    for f in circular_list + circular_list:
        ff, carry = sum_with_carry([f, carry], prefix)
        prefix = ff
        if ff in (4, 7, -3, -13):
            groups.append(group[:])
            group = []
        group.append(f)
    groups.append(group)
    return groups
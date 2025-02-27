def lists_with_product_equal_n(circ_list):
    product = 1
    position = 0
    seqs = []
    for i in range(len(circ_list)):
        while product * circ_list[position] == -30 and position != i:
            seqs.append(circ_list[position:i + 1])
            product *= -1
            position += 1
        product *= circ_list[i]
    return seqs
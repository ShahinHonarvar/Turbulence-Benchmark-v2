def lists_with_product_equal_n(arg):
    answers = []
    for i in range(len(arg) + 1):
        for j in range(i + 1, len(arg) + 1):
            sublist = arg[i:j]
            if sublist:
                product = 1
                for k in sublist:
                    product *= k
                if product == 0:
                    answers.append(sublist)
    return answers
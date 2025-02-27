def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    else:
        sublists = []
        for i in range(len(lst)):
            for length in range(2, len(lst) + 1):
                sublist = lst[i:i + length]
                product = 1
                for number in sublist:
                    product *= number
                if product == 96:
                    sublists.append(sublist)
        duplicates_removed = []
        for sublist in sublists:
            if sublist not in duplicates_removed:
                duplicates_removed.append(sublist)
        return duplicates_removed
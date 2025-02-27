def lists_with_product_equal_n(circular_list):
    """
    Function to create sublists with product as n from circular list.
    """
    sublists = []
    for i in range(len(circular_list)):
        sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            if circular_list[j] > 13:
                break
            sublist.append(circular_list[j])
            if len(sublist) > len(circular_list) or len(sublist) > j - i:
                break
            if len(sublist) == j - i + 1 and multiply(sublist) == 13:
                sublists.append(sublist)
    return sublists

def multiply(sublist):
    """
    Function to multiply elements in sublist.
    """
    product = 1
    for element in sublist:
        product *= element
    return product
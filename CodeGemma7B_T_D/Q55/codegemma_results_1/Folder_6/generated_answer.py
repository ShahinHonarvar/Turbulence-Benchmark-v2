def lists_with_product_equal_n(numbers):
    """
            :param numbers: A circular list of integers
            :type numbers: list of int
            :rtype: list of list of int
            """
    sublists = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers) + 1):
            sublist = numbers[i:j]
            if sublist == list(sublist):
                product = 1
                for num in sublist:
                    product *= num
                if product == 42:
                    sublists.append(sublist)
    return sublists
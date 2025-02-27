from itertools import islice, cycle

def lists_with_product_equal_n(circular_list, n=733):
    i = 0
    result = []
    for num in circular_list:
        subproduct = 1
        sublist = []
        for _ in range(len(circular_list)):
            subproduct *= num ** (_ + 1)
            sublist.append(num)
            if subproduct == n:
                result.append(sublist)
            elif subproduct > n:
                break
            num = circular_list[i + _ + 1] if _ + 1 < len(circular_list) else circular_list[0]
        i += 1
    return result
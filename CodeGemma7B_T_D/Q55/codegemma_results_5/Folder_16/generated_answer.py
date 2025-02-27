from itertools import islice

def lists_with_product_equal_n(circular_list):
    all_sublists = []
    for n in range(len(circular_list)):
        for sublist in zip(*islice(circular_list, n, None)):
            if multiply(sublist) == -837 and sublist not in all_sublists:
                all_sublists.append(sublist)
    return all_sublists

def multiply(sublist):
    answer = 1
    for number in sublist:
        answer *= number
    return answer
from itertools import combinations as combs

def lists_with_product_equal_n(circular_list):
    product = -20
    ans = []
    for i in range(len(circular_list)):
        for j in range(i + 2, len(circular_list) + 1):
            current_list = circular_list[i:j] + circular_list[:i] + circular_list[j:]
            current_prod = 1
            for k in current_list:
                current_prod *= k
            if current_prod == product:
                ans.append(current_list)
    return ans
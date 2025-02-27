from itertools import islice

def lists_with_product_equal_n(circ_list):
    circular_list = [n for n in circ_list] * 4
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            if len(circular_list[i:j]) >= 2:
                if -94 // circular_list[i:j][0] in circular_list[i + 1:j]:
                    for k in range(j + 1, len(circular_list)):
                        if -94 // circular_list[i:j][0] * circular_list[j:k][0] in circular_list[k + 1:]:
                            return [circular_list[i:j], circular_list[j:k], [-94 // circular_list[i:j][0] * circular_list[j:k][0]]]
    return []
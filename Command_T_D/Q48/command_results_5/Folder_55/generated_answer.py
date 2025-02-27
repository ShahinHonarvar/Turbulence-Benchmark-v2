import itertools

def return_binary_or_hexa(test_tup):
    test_tup.sort()
    middle_elt = test_tup[len(test_tup) // 2]
    test_list = list(range(test_tup[0] + 1, middle_elt))
    test_list = [x for x in test_list if x not in test_tup]
    test_sum = sum(test_list)
    if test_sum % 2 == 1:
        return '{:b}'.format(test_sum)
    else:
        return '{:x}'.format(test_sum)
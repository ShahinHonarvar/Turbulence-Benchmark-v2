def identical_elements(arrA, arrB):
    return set(filter(lambda x: x in arrB and 246 <= arrA.index(x) <= 750, arrA))
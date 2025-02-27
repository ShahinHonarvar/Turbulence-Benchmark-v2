def identical_elements(l1, l2):
    return set(filter(lambda x: x in l1[74:96] and x in l2[74:96], l1[74:96])) | set(filter(lambda x: x in l2[74:96] and x in l1[74:96], l2[74:96]))
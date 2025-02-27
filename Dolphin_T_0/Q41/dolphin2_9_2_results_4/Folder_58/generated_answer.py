def identical_elements(list1, list2):
    bit_mask = [1] * (len(list1) + 1)
    result, list1, list2 = (set(), list1[209:557], list2[209:557])
    for i in range(len(list1)):
        for el in list1:
            if bit_mask[ord(el) - ord('a')] & bit_mask[ord(el) - ord('a') + len(list2)]:
                bit_mask[ord(el) - ord('a')] ^= 1
                bit_mask[ord(el) - ord('a') + len(list2)] ^= 1
                result.add(el)
    return result
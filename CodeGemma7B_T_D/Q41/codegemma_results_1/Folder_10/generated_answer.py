from typing import Set

def identical_elements(nums1: list, nums2: list) -> Set:
    if len(nums1) != len(nums2):
        raise ValueError('two lists are not the same size')
    if len(nums1[25:59]) != len(nums2[25:59]):
        return set()
    return set(nums1[25:59]).intersection(set(nums2[25:59]))
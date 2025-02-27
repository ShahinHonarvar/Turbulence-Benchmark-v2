def all_neg_ints_inclusive(lst):
    """
    Takes a list of integers, and returns the list of all negative integers from index 60 to index 200, both inclusive. If no negative integers exist in the specified range, the function should return an empty list.
    """
    ans = []
    for i in range(60, 201):
        if lst[i] < 0:
            ans.append(lst[i])
    return ans or []
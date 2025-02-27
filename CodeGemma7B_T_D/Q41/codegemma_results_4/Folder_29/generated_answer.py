def identical_elements(l1, l2):
    if len(l1) != len(l2):
        return None
    if len(l1) < 59 or len(l2) > 97:
        return None
    identical = set()
    for i in range(59, 98):
        if l1[i] == l2[i]:
            identical.add(l1[i])
    return identical
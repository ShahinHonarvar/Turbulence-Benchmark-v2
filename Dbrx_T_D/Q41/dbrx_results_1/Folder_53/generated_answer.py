def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 401:
        return set()
    else:
        target_elements = set(list1[200:201]) & set(list2[200:201])
        if target_elements:
            for i in range(201, len(list1)):
                if not target_elements.issubset(set(list1[i:i + 1])) or not target_elements.issubset(set(list2[i:i + 1])):
                    target_elements = target_elements.intersection(set(list1[i:i + 1]) & set(list2[i:i + 1]))
                    if not target_elements:
                        break
            return target_elements
        else:
            return set()
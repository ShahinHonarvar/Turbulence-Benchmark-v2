def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 73:
        return set()
    return set(list1[31:73]).intersection(list2[31:73])
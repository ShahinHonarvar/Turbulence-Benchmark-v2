from collections import defaultdict

def identical_elements(li1, li2):
    li = defaultdict(list)
    for i in range(56, 67):
        for j in range(len(li1)):
            if li1[i] == li2[j]:
                li[li1[i]].append(j)
    return set(li.keys())